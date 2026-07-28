(function () {
  const form = document.getElementById('calcForm');

  const els = {
    payTypeRadios: form.querySelectorAll('input[name="payType"]'),
    salaryField: document.getElementById('salaryField'),
    salary: document.getElementById('salary'),
    hourlyField: document.getElementById('hourlyField'),
    hourlyRate: document.getElementById('hourlyRate'),
    hoursWeeksField: document.getElementById('hoursWeeksField'),
    hoursPerWeek: document.getElementById('hoursPerWeek'),
    weeksPerYear: document.getElementById('weeksPerYear'),
    impacted: document.getElementById('impacted'),
    impactedVal: document.getElementById('impactedVal'),
    ampTypeRadios: form.querySelectorAll('input[name="ampType"]'),
    timeSavedField: document.getElementById('timeSavedField'),
    timeSaved: document.getElementById('timeSaved'),
    timeSavedVal: document.getElementById('timeSavedVal'),
    multiplierField: document.getElementById('multiplierField'),
    multiplier: document.getElementById('multiplier'),
    quality: document.getElementById('quality'),
    qualityVal: document.getElementById('qualityVal'),
    toolCost: document.getElementById('toolCost'),
    learningHours: document.getElementById('learningHours'),
    educationCost: document.getElementById('educationCost'),
    improvementFactor: document.getElementById('improvementFactor'),
    improvementFactorVal: document.getElementById('improvementFactorVal'),
    currencyInputs: form.querySelectorAll('.currency-input'),
  };

  const out = {
    annualCost: document.getElementById('outAnnualCost'),
    annualValue: document.getElementById('outAnnualValue'),
    aiCost: document.getElementById('outAiCost'),
    netValue: document.getElementById('outNetValue'),
    updatedLaborValue: document.getElementById('outUpdatedLaborValue'),
    updatedLaborValuePct: document.getElementById('outUpdatedLaborValuePct'),
    roi: document.getElementById('outRoi'),
    hoursSaved: document.getElementById('outHoursSaved'),
  };

  const currency = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    maximumFractionDigits: 0,
  });

  function num(el, fallback) {
    const raw = String(el.value).replace(/[^0-9.]/g, '');
    const v = parseFloat(raw);
    if (isNaN(v) || v < 0) return fallback;
    return v;
  }

  function formatCurrencyInput(el) {
    const caretFromEnd = el.value.length - el.selectionEnd;
    const raw = el.value.replace(/[^0-9.]/g, '');
    if (raw === '') return;
    const [intRaw, decRaw] = raw.split('.');
    const intPart = intRaw.replace(/^0+(?=\d)/, '');
    let formatted = Number(intPart || '0').toLocaleString('en-US');
    if (decRaw !== undefined) {
      formatted += '.' + decRaw.slice(0, 2);
    }
    el.value = formatted;
    const newPos = Math.max(formatted.length - caretFromEnd, 0);
    el.setSelectionRange(newPos, newPos);
  }

  function getPayType() {
    return form.querySelector('input[name="payType"]:checked').value;
  }

  function getAmpType() {
    return form.querySelector('input[name="ampType"]:checked').value;
  }

  function updateVisibility() {
    const payType = getPayType();
    els.salaryField.classList.toggle('hidden', payType !== 'salary');
    els.hourlyField.classList.toggle('hidden', payType !== 'hourly');
    els.hoursWeeksField.classList.toggle('hidden', payType !== 'hourly');

    const ampType = getAmpType();
    els.timeSavedField.classList.toggle('hidden', ampType !== 'timesaved');
    els.multiplierField.classList.toggle('hidden', ampType !== 'multiplier');
  }

  function calculate() {
    const payType = getPayType();
    const ampType = getAmpType();

    // Hours/week and weeks/year are always used as the basis for the
    // effective hourly rate (learning-time cost), even for salaried pay.
    const hoursPerWeek = num(els.hoursPerWeek, 40);
    const weeksPerYear = num(els.weeksPerYear, 50);

    // 1. Annual labor cost
    let annualCost;
    if (payType === 'salary') {
      annualCost = num(els.salary, 0);
    } else {
      const hourlyRate = num(els.hourlyRate, 0);
      annualCost = hourlyRate * hoursPerWeek * weeksPerYear;
    }

    // 2. Time-saved fraction (normalized from either input mode)
    let timeSavedFraction;
    if (ampType === 'timesaved') {
      timeSavedFraction = num(els.timeSaved, 0) / 100;
    } else {
      const m = Math.max(1, num(els.multiplier, 1));
      timeSavedFraction = 1 - 1 / m;
    }

    // 3. Base annual value created (time saved + quality, scaled by impacted work)
    const impactedFraction = num(els.impacted, 0) / 100;
    const qualityFraction = num(els.quality, 15) / 100;
    const baseAnnualValue = annualCost * impactedFraction * (timeSavedFraction + qualityFraction);

    // 3b. Apply monthly improvement factor: multiplier grows linearly from
    // 1.00 in month 1 to 1 + 11*rate in month 12, which averages out to
    // a flat growth factor of 1 + 5.5*rate across the year.
    const improvementRate = num(els.improvementFactor, 1) / 100;
    const growthFactor = 1 + 5.5 * improvementRate;
    const annualValue = baseAnnualValue * growthFactor;

    // 4. Tool, education & learning-time cost
    const monthlyToolCost = num(els.toolCost, 0);
    const monthlyEducationCost = num(els.educationCost, 0);
    const annualDirectAiCost = (monthlyToolCost + monthlyEducationCost) * 12;

    const effectiveHourlyRate = hoursPerWeek * weeksPerYear > 0
      ? annualCost / (hoursPerWeek * weeksPerYear)
      : 0;
    const learningHoursPerWeek = num(els.learningHours, 0);
    const annualLearningTimeCost = learningHoursPerWeek * weeksPerYear * effectiveHourlyRate;

    const annualAiCost = annualDirectAiCost + annualLearningTimeCost;

    // 5. Net value & ROI
    const netAnnualValue = annualValue - annualAiCost;

    // 5b. Updated labor value: what the labor is worth once net AI value is folded in
    const updatedLaborValue = annualCost + netAnnualValue;
    const laborValuePctText = annualCost === 0
      ? 'N/A'
      : `${netAnnualValue >= 0 ? '+' : ''}${((netAnnualValue / annualCost) * 100).toFixed(0)}%`;

    let roiText;
    if (annualAiCost === 0) {
      roiText = annualValue > 0 ? '∞' : 'N/A';
    } else {
      const roi = (netAnnualValue / annualAiCost) * 100;
      roiText = `${roi >= 0 ? '+' : ''}${roi.toFixed(0)}%`;
    }

    // 6. Total hours saved per year
    const hoursWorkedPerYear = hoursPerWeek * weeksPerYear;
    const hoursSavedPerYear = hoursWorkedPerYear * impactedFraction * timeSavedFraction * growthFactor;
    const hoursSavedText = `${hoursSavedPerYear.toFixed(0)} hrs/yr`;

    // Render
    out.annualCost.textContent = currency.format(annualCost);
    out.annualValue.textContent = currency.format(annualValue);
    out.aiCost.textContent = currency.format(annualAiCost);
    out.netValue.textContent = currency.format(netAnnualValue);
    out.netValue.classList.toggle('negative', netAnnualValue < 0);
    out.updatedLaborValue.textContent = currency.format(updatedLaborValue);
    out.updatedLaborValuePct.textContent = laborValuePctText;
    out.updatedLaborValuePct.classList.remove('positive', 'negative');
    if (laborValuePctText !== 'N/A') {
      out.updatedLaborValuePct.classList.add(netAnnualValue >= 0 ? 'positive' : 'negative');
    }
    out.roi.textContent = roiText;
    out.hoursSaved.textContent = hoursSavedText;

    out.roi.classList.remove('positive', 'negative');
    if (roiText !== 'N/A' && roiText !== '∞') {
      out.roi.classList.add(netAnnualValue >= 0 ? 'positive' : 'negative');
    }
  }

  function updateLiveLabels() {
    els.impactedVal.textContent = `${els.impacted.value}%`;
    els.timeSavedVal.textContent = `${els.timeSaved.value}%`;
    els.qualityVal.textContent = `${els.quality.value}%`;
    els.improvementFactorVal.textContent = `${els.improvementFactor.value}%`;
  }

  function refresh() {
    updateVisibility();
    updateLiveLabels();
    calculate();
  }

  els.currencyInputs.forEach((el) => {
    el.addEventListener('input', () => formatCurrencyInput(el));
  });

  form.addEventListener('input', refresh);
  els.payTypeRadios.forEach((r) => r.addEventListener('change', refresh));
  els.ampTypeRadios.forEach((r) => r.addEventListener('change', refresh));

  document.getElementById('year').textContent = new Date().getFullYear();

  refresh();
})();
