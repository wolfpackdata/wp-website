/* ==========================================================================
   Wolfpack case studies — the transaction map.

   Time on the x-axis, four industry lanes on the y, one dot per event, every
   label packed into the lowest free track in its lane. No dependencies.

   ONE SCRIPT, ONE DATASET, TWO PAGES. The report embeds this map at a fixed
   width inside a horizontal scroller; transaction-map.html renders the same
   map full width in its own tab. Both read the EVENTS array below.

   That is not tidiness, it is the whole reason this file exists. The source
   these pages were rebuilt from shipped the map twice as two copies of the same
   two hundred lines, and the copies had already drifted: the standalone plotted
   the April 2025 tariff event and the embedded one did not, so the same figure
   told two different stories depending on which tab you opened. Nothing in that
   build could have noticed. Any change to the data or the packing now lands on
   both, or on neither.

   NOTHING IS HAND-PLACED. Every position is computed from the dates and from
   the measured width of the labels, which is what lets the figure survive a
   resize, a font substitution, and a repalette without anybody re-tuning it.
   If you ever find yourself nudging a label, the packing pass is the thing to
   fix.

   LABELS ARE MEASURED, NOT ESTIMATED. The original approximated each label's
   width as `label.length * 5.75 + 34`. That is a guess about a font, and the
   font here is --mono: a SYSTEM stack, so its metrics are whatever the reader's
   machine happens to resolve — unknowable from the machine this was built on.
   A guess that runs narrow packs two labels into one track and they overlap; a
   guess that runs wide wastes a track per lane. So the width comes from
   canvas measureText using the element's own computed font, with the old
   estimate kept as the fallback for a browser that gives us no 2d context.

   REDUCED MOTION: there is no motion here to bypass. The map is drawn once and
   redrawn on resize; nothing animates, nothing transitions, nothing scrolls by
   itself. The only thing that moves is the reader's own scrollbar.
   ========================================================================== */

(function () {
  'use strict';

  /* ---- The lanes ---------------------------------------------------------
     Lane assignment reflects where in the industry a transaction LANDED, not
     the acquirer's home category. Boris FX is a visual-effects company and its
     iZotope purchase sits in "software & platform", because that is the market
     it changed. */
  var LANES = [
    'Macro & regulatory',
    'Software & platform',
    'Hardware manufacturing',
    'Retail & marketplace'
  ];

  /* ---- The deal-value scale ----------------------------------------------
     Ordered and sequential: one neutral ramp, dark to light on a dark ground,
     because the variable is a magnitude. Index 0 is NOT the bottom of the ramp
     — it is "undisclosed", drawn as an unfilled ring, because an absent value
     is not a small one. The tokens are declared and contrast-measured in
     case-study.css. */
  var FILL = [
    'transparent',
    'var(--fig-ramp-1)',   /* 1 · < $100m      */
    'var(--fig-ramp-2)',   /* 2 · $100 – 499m  */
    'var(--fig-ramp-3)',   /* 3 · $500 – 999m  */
    'var(--fig-ramp-4)'    /* 4 · ≥ $1bn       */
  ];

  /* ---- The events --------------------------------------------------------
     [decimal year, lane index, label, value bucket]

     Placed by announcement date. Decimal years are approximate within a year
     where only the year is known, which is why the axis is labelled by year and
     not by month. Values are the disclosed or reported headline consideration
     in USD; Sonova/Sennheiser (€200m ≈ $236m) is bucketed on its converted
     value. Every row here is also a row in one of the three era tables in the
     report, with its own source link — the map adds shape, never a fact. */
  var EVENTS = [
    /* Macro & regulatory */
    [2024.55, 0, 'NZCC blocks AlphaTheta/Serato', 0],
    [2025.27, 0, 'US tariffs: China MI duty ~11% → 145%', 0],

    /* Software & platform */
    [2021.50, 1, 'Francisco Partners → Native Instruments', 0],
    [2022.25, 1, 'Francisco Partners → Plugin Alliance/bx', 0],
    [2022.60, 1, 'Audiotonix → Slate Digital', 0],
    [2022.95, 1, 'Focusrite → Sonnox', 0],
    [2023.50, 1, 'AlphaTheta → Serato (announced)', 0],
    [2023.60, 1, 'SSL → Harrison · Audiotonix → Fourier', 0],
    [2023.85, 1, 'STG → Avid · $1.4bn', 4],
    [2026.07, 1, 'Native Instruments insolvency', 0],
    [2026.35, 1, 'inMusic → Native Instruments', 0],
    [2026.50, 1, 'Boris FX → iZotope', 0],
    [2026.54, 1, 'Dirk Ulrich → Plugin Alliance/bx', 0],

    /* Hardware manufacturing */
    [2014.50, 2, 'KKR → Pioneer DJ · $551m', 3],
    [2017.20, 2, 'Samsung → Harman · $8bn', 4],
    [2017.70, 2, 'Audiotonix → SSL', 0],
    [2018.40, 2, 'Audiotonix → KLANG', 0],
    [2018.80, 2, 'Gibson exits Chapter 11', 0],
    [2019.55, 2, 'Focusrite → ADAM Audio', 0],
    [2019.90, 2, 'Focusrite → Martin Audio', 0],
    [2020.02, 2, 'Pioneer DJ renames AlphaTheta', 0],
    [2020.14, 2, 'Servco → Fender majority', 0],
    [2020.22, 2, 'Noritsu → AlphaTheta · $606m', 3],
    [2020.30, 2, 'Ardian → Audiotonix', 0],
    [2021.35, 2, 'Sonova → Sennheiser Consumer · $236m', 2],
    [2021.65, 2, 'Audiotonix → Sound Devices', 0],
    [2021.85, 2, 'Fender → PreSonus', 0],
    [2022.05, 2, 'Masimo → Sound United · $1.03bn', 4],
    [2022.40, 2, 'Focusrite → Sequential/Oberheim', 0],
    [2022.70, 2, 'Roland → Drum Workshop · $65m', 1],
    [2023.25, 2, 'Zound + Marshall merge', 0],
    [2023.30, 2, 'Bose → Transom (Bose Pro)', 0],
    [2023.45, 2, 'inMusic → Moog Music', 0],
    [2024.30, 2, 'PAI → Audiotonix (from Ardian)', 0],
    [2025.72, 2, 'Masimo → Harman · $350m', 2],
    [2026.09, 2, 'Audiotonix → DPA/Wisycom/Austrian', 0],
    [2026.20, 2, 'Sennheiser Consumer re-listed', 0],

    /* Retail & marketplace */
    [2019.40, 3, 'Etsy → Reverb · $275m', 2],
    [2020.87, 3, 'Guitar Center Chapter 11', 0],
    [2021.55, 3, 'Providence → Sweetwater', 0],
    [2025.42, 3, 'Etsy sells Reverb · $105m', 2],
    [2025.60, 3, 'Guitar Center refinances to 2029', 0]
  ];

  /* ---- The macro bands ---------------------------------------------------
     Shocks, not transactions. They are drawn as a flat wash behind the lanes
     with the label in a reserved strip above them, so they share no shape and
     no fill with a dot. */
  var BANDS = [
    [2020.20, 2022.00, 'Pandemic demand surge'],
    [2025.25, 2026.75, 'US tariffs · 10% universal → 145% China']
  ];

  /* ---- Geometry ---------------------------------------------------------- */
  var X0 = 2014.0, X1 = 2026.9;   // the axis, linear, in decimal years
  var LEFT = 14;                  // inset before the first gridline
  var RESERVE = 190;              // room past the axis for a right-hand label
  var MIN_PLOT = 1600;            // never compresses below this — it scrolls
  var ROW = 24;                   // one label track
  var LANE_PAD = 34;              // room for the lane name above its first track
  var AXIS = 32;                  // the year labels below the last lane
  var HEAD = 26;                  // the reserved strip the band labels sit in
  var GUTTER = 8;                 // clear space demanded between two label spans
  var MAX_TRACKS = 16;            // a backstop; no lane comes close

  /* ---- Label width, measured ---------------------------------------------
     One canvas for the life of the page. The font string is read off a real
     .map__lab element so the measurement is of the face the browser actually
     resolved from the --mono stack, not of a face this file guessed at. */
  function measurer(host) {
    var probe = document.createElement('span');
    probe.className = 'map__lab';
    probe.style.position = 'absolute';
    probe.style.visibility = 'hidden';
    host.appendChild(probe);
    var cs = window.getComputedStyle(probe);
    var font = cs.fontStyle + ' ' + cs.fontWeight + ' ' + cs.fontSize + ' / ' +
               cs.lineHeight + ' ' + cs.fontFamily;
    host.removeChild(probe);

    var ctx = null;
    try {
      ctx = document.createElement('canvas').getContext('2d');
      if (ctx) ctx.font = font;
    } catch (e) { ctx = null; }

    // 34px covers the dot, the flex gap, and a little slack past the text.
    return function (label) {
      if (ctx) return ctx.measureText(label).width + 34;
      return label.length * 5.75 + 34;   // the old estimate, as a fallback only
    };
  }

  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  /* A label like "STG → Avid · $1.4bn" gets its figure set in the brighter
     ink, so a value can be picked out of a lane without reading every word. */
  function markup(label) {
    return esc(label).replace(/·\s(\$[^\s]+)/, '· <b>$1</b>');
  }

  function init(host) {
    var scroller = host.closest ? host.closest('.map__scroll') : host.parentNode;
    var fill = host.getAttribute('data-fill') === 'true';
    var width = measurer(host);

    function render() {
      // Fixed inside the report; spread to the tab on the standalone page. The
      // floor is the same in both, so the packing never has to cope with a
      // width at which forty-two labels cannot be read.
      var plot = MIN_PLOT;
      if (fill && scroller) {
        plot = Math.max(MIN_PLOT, scroller.clientWidth - RESERVE - 30);
      }

      function px(year) { return LEFT + (year - X0) / (X1 - X0) * plot; }

      /* ---- Pack ---------------------------------------------------------
         Events sort by date. Each label sits to the RIGHT of its dot, flipping
         LEFT when the pair would run past the plot's right edge. It then takes
         the lowest track in its lane whose occupied spans it does not touch,
         with GUTTER of clear space demanded on each side. The lane grows to
         fit however many tracks that needs. */
      var byLane = {};
      EVENTS.slice()
        .sort(function (a, b) { return a[0] - b[0]; })
        .forEach(function (e) {
          (byLane[e[1]] = byLane[e[1]] || []).push(e);
        });

      var laid = {}, laneTracks = {};
      Object.keys(byLane).forEach(function (lane) {
        var tracks = [], out = [];
        byLane[lane].forEach(function (e) {
          var x = px(e[0]);
          var w = width(e[2]);
          var side = (x + w > plot + LEFT - 4) ? 'left' : 'right';
          var start = side === 'right' ? x : x - w;
          var end   = side === 'right' ? x + w : x;

          var t = 0;
          while (true) {
            var occupied = tracks[t] || [], free = true;
            for (var i = 0; i < occupied.length; i++) {
              if (start < occupied[i][1] + GUTTER && end > occupied[i][0] - GUTTER) {
                free = false;
                break;
              }
            }
            if (free) { (tracks[t] = occupied).push([start, end]); break; }
            t++;
            if (t > MAX_TRACKS) { (tracks[t] = []).push([start, end]); break; }
          }
          out.push({ x: x, t: t, side: side, label: e[2], bucket: e[3] });
        });
        laid[lane] = out;
        laneTracks[lane] = tracks.length;
      });

      /* ---- Lay the lanes out vertically --------------------------------- */
      var html = '', top = HEAD, laneTops = [];
      for (var L = 0; L < LANES.length; L++) {
        var n = laneTracks[L] || 1;
        laneTops.push({ top: top, h: n * ROW + LANE_PAD + 8 });
        top += n * ROW + LANE_PAD + 8;
      }
      var totalH = top + AXIS;
      var plotH = top - HEAD;

      /* ---- Bands and gridlines, behind everything ----------------------- */
      BANDS.forEach(function (b) {
        var l = px(b[0]), r = px(b[1]);
        html += '<div class="map__band" style="left:' + l + 'px; width:' + (r - l) +
                'px; top:' + HEAD + 'px; height:' + plotH + 'px">' +
                '<span>' + esc(b[2]) + '</span></div>';
      });
      for (var y = 2014; y <= 2026; y++) {
        html += '<div class="map__grid" style="left:' + px(y) + 'px; top:' + HEAD +
                'px; height:' + plotH + 'px"></div>';
        html += '<div class="map__yr" style="left:' + px(y) + 'px">' + y + '</div>';
      }

      /* ---- Lanes and events --------------------------------------------- */
      for (var L2 = 0; L2 < LANES.length; L2++) {
        var lt = laneTops[L2];
        html += '<div class="map__lane' + (L2 % 2 ? ' map__lane--alt' : '') +
                '" style="position:absolute; left:0; right:0; top:' + lt.top +
                'px; height:' + lt.h + 'px">' +
                '<div class="map__lname">' + esc(LANES[L2]) + '</div></div>';

        (laid[L2] || []).forEach(function (d) {
          var yTop = lt.top + LANE_PAD + d.t * ROW - 6;
          var pos = d.side === 'right'
            ? 'left:' + d.x + 'px; transform:translateX(-5px)'
            : 'left:' + d.x + 'px; transform:translateX(-100%) translateX(5px)';
          html += '<div class="map__ev' + (d.side === 'left' ? ' map__ev--left' : '') +
                  '" style="' + pos + '; top:' + yTop + 'px">' +
                  '<span class="map__dot" style="background:' + FILL[d.bucket] + '"></span>' +
                  '<span class="map__lab">' + markup(d.label) + '</span></div>';
        });
      }

      host.style.width = (plot + LEFT + RESERVE) + 'px';
      host.style.height = totalH + 'px';
      host.innerHTML = html;
      if (scroller) scroller.classList.add('is-drawn');
    }

    render();

    // Only the spreading copy has anything to recompute; the embedded one is a
    // fixed width by design and redrawing it would be work that changes
    // nothing.
    //
    // A ResizeObserver on the SCROLLER, not a listener on the window. The plot
    // width is computed from the scroller's width, so the scroller is the thing
    // whose changes matter — and it can change without the window resizing at
    // all (a zoom step, a print stylesheet, a device rotation that headless
    // reports differently, this page embedded in a frame that is resized around
    // it). Observing the window instead means the figure is correct only for
    // the one cause of a width change that happens to be the most obvious.
    // No feedback loop: render() writes a width on the HOST inside the
    // scroller, which does not change the scroller's own width.
    // The window listener stays as the fallback for anything without RO.
    if (fill) {
      var timer = null;
      var debounced = function () {
        clearTimeout(timer);
        timer = setTimeout(render, 140);
      };
      // Both, deliberately, and they share one timer so two signals for the
      // same change still produce one render.
      window.addEventListener('resize', debounced);
      if (scroller && typeof ResizeObserver === 'function') {
        new ResizeObserver(debounced).observe(scroller);
      }
    }
  }

  var hosts = document.querySelectorAll('.map');
  for (var i = 0; i < hosts.length; i++) init(hosts[i]);
}());
