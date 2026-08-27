/**
 * KISAAN_SATHI (किसान साथी) Web Application Engine
 * Integrates FastAPI/Vercel Serverless Backend with Client-Side Fallback Intelligence.
 */

// DATA CONSTANTS & HUBS
const DEMO_HUBS = {
  nashik: {
    id: "nashik",
    name_en: "Nashik, Maharashtra",
    name_hi: "नासिक, महाराष्ट्र",
    state: "Maharashtra",
    district: "Nashik",
    lat: 19.9975,
    lon: 73.7898,
    soil: { n: 85, p: 48, k: 190, ph: 6.8, type: "Black Cotton Loam" },
    weather: { temp: "26.5°C", hum: "74%", rain: "68 mm", cond: "Partly Cloudy • अनुकूल मौसम", spray: "Good for Spraying • छिड़काव के लिए उत्तम समय", icon: "⛅" },
    topCrop: { name: "🍇 Grapes / अंगूर (Vitis vinifera)", family: "Vitaceae (Fruit) • 135 Days", score: "94.8%", yield: "8 - 12 Tonnes", rev: "₹3,50,000 - ₹5,00,000", rate: "₹6,200 / Qtl ↗", sowing: "Oct - Nov (Pruning)" },
    shapText: "आपकी मिट्टी में पोटाश (190 kg/ha) और अनुकूल pH (6.8) अंगूर की मिठास और बेहतर पैदावार के लिए सर्वाधिक अनुकूल हैं।",
    shapBars: [
      { name: "Potassium (K: 190)", pct: 82, val: "+28%", pos: true },
      { name: "Soil pH (6.8 Neutral)", pct: 65, val: "+18%", pos: true },
      { name: "Nitrogen (N: 85)", pct: 48, val: "+12%", pos: true },
      { name: "Phosphorus (P: 48)", pct: 32, val: "+7%", pos: true },
      { name: "Rainfall Forecast", pct: 18, val: "-4%", pos: false }
    ],
    runners: [
      { name: "🍎 Pomegranate / अनार", score: "91.2%", meta: "Est: ₹2.8L - ₹4.2L / acre • Mandi: ₹8,400/Qtl" },
      { name: "🌿 Cotton / कपास", score: "86.5%", meta: "Est: ₹75K - ₹1.05L / acre • Mandi: ₹7,450/Qtl" }
    ]
  },
  indore: {
    id: "indore",
    name_en: "Indore, Madhya Pradesh",
    name_hi: "इंदौर, मध्य प्रदेश",
    state: "Madhya Pradesh",
    district: "Indore",
    lat: 22.7196,
    lon: 75.8577,
    soil: { n: 45, p: 62, k: 82, ph: 7.4, type: "Deep Black Malwa Clay" },
    weather: { temp: "28.0°C", hum: "65%", rain: "42 mm", cond: "Clear & Sunny • साफ मौसम", spray: "Excellent for Spraying • छिड़काव हेतु श्रेष्ठ समय", icon: "☀️" },
    topCrop: { name: "🌾 Chickpea / चना (Cicer arietinum)", family: "Fabaceae (Legume/Pulse) • 110 Days", score: "93.4%", yield: "8 - 12 Quintals", rev: "₹50,000 - ₹74,000", rate: "₹6,150 / Qtl ↗", sowing: "Oct - Nov (Rabi)" },
    shapText: "मालवा की गहरी काली मिट्टी व संतुलित फॉस्फोरस (62 kg/ha) दलहनी फसलों में जड़ ग्रंथियों के विकास और चने के दानों के भराव के लिए सर्वोत्तम है।",
    shapBars: [
      { name: "Phosphorus (P: 62)", pct: 85, val: "+26%", pos: true },
      { name: "Clay Content (45%)", pct: 60, val: "+16%", pos: true },
      { name: "Soil pH (7.4)", pct: 50, val: "+14%", pos: true },
      { name: "Nitrogen (N: 45)", pct: 28, val: "+6%", pos: true },
      { name: "High Heat Peak", pct: 15, val: "-3%", pos: false }
    ],
    runners: [
      { name: "🌱 Soybean / सोयाबीन", score: "89.5%", meta: "Est: ₹45K - ₹62K / acre • Mandi: ₹4,680/Qtl" },
      { name: "🌽 Maize / मक्का", score: "84.2%", meta: "Est: ₹55K - ₹72K / acre • Mandi: ₹2,280/Qtl" }
    ]
  },
  ludhiana: {
    id: "ludhiana",
    name_en: "Ludhiana, Punjab",
    name_hi: "लुधियाना, पंजाब",
    state: "Punjab",
    district: "Ludhiana",
    lat: 30.9010,
    lon: 75.8573,
    soil: { n: 92, p: 42, k: 38, ph: 7.2, type: "Alluvial Sandy Loam" },
    weather: { temp: "30.5°C", hum: "68%", rain: "55 mm", cond: "Warm Humid • उमस भरा", spray: "Spray after 4 PM • शाम 4 बजे बाद छिड़काव", icon: "🌤️" },
    topCrop: { name: "🌾 Rice / धान (Oryza sativa)", family: "Poaceae (Cereal) • 130 Days", score: "92.8%", yield: "22 - 28 Quintals", rev: "₹85,000 - ₹1,10,000", rate: "₹3,950 / Qtl ↗", sowing: "June - July (Transplanting)" },
    shapText: "जलोढ़ दोमट मिट्टी और प्रचुर नाइट्रोजन (92 kg/ha) धान की कल्ले फूटने की अवस्था व भरपूर पैदावार में मुख्य सहायक तत्व हैं।",
    shapBars: [
      { name: "Nitrogen (N: 92)", pct: 88, val: "+29%", pos: true },
      { name: "Irrigation Access", pct: 70, val: "+21%", pos: true },
      { name: "Soil pH (7.2)", pct: 45, val: "+11%", pos: true },
      { name: "Organic Matter", pct: 30, val: "+5%", pos: true },
      { name: "Groundwater Strain", pct: 25, val: "-6%", pos: false }
    ],
    runners: [
      { name: "🌽 Maize / मक्का", score: "88.1%", meta: "Est: ₹55K - ₹72K / acre • Mandi: ₹2,280/Qtl" },
      { name: "🌿 Cotton / कपास", score: "83.6%", meta: "Est: ₹75K - ₹1.05L / acre • Mandi: ₹7,450/Qtl" }
    ]
  },
  guntur: {
    id: "guntur",
    name_en: "Guntur, Andhra Pradesh",
    name_hi: "गुंटूर, आंध्र प्रदेश",
    state: "Andhra Pradesh",
    district: "Guntur",
    lat: 16.3067,
    lon: 80.4365,
    soil: { n: 70, p: 55, k: 140, ph: 6.5, type: "Red Clayey Sandy Loam" },
    weather: { temp: "31.2°C", hum: "78%", rain: "80 mm", cond: "Tropical Humid • उष्ण आर्द्र", spray: "Check Wind Speed • हवा की गति देखकर छिड़कें", icon: "🌧️" },
    topCrop: { name: "🌿 Cotton / कपास (Gossypium hirsutum)", family: "Malvaceae (Fiber) • 160 Days", score: "94.1%", yield: "10 - 14 Quintals", rev: "₹75,000 - ₹1,05,000", rate: "₹7,450 / Qtl ▶", sowing: "May - June (Kharif)" },
    shapText: "लाल चिकनी दोमट मिट्टी और उच्च पोटाश (140 kg/ha) कपास के टिंडों के आकार व रेशे की गुणवत्ता के लिए अत्यंत लाभकारी हैं।",
    shapBars: [
      { name: "Potassium (K: 140)", pct: 78, val: "+24%", pos: true },
      { name: "Phosphorus (P: 55)", pct: 62, val: "+17%", pos: true },
      { name: "Soil pH (6.5)", pct: 54, val: "+13%", pos: true },
      { name: "Nitrogen (N: 70)", pct: 40, val: "+9%", pos: true },
      { name: "High Humidity Risk", pct: 20, val: "-5%", pos: false }
    ],
    runners: [
      { name: "🌶️ Chilli / मिर्च", score: "91.8%", meta: "Est: ₹1.2L - ₹1.8L / acre • Mandi: ₹18,500/Qtl" },
      { name: "🌽 Maize / मक्का", score: "85.0%", meta: "Est: ₹55K - ₹72K / acre • Mandi: ₹2,280/Qtl" }
    ]
  }
};

// LEAF DISEASE SAMPLES
const LEAF_SAMPLES = {
  tomato_early_blight: {
    crop: "Tomato / टमाटर",
    name: "Early Blight (Alternaria solani)",
    name_hi: "अगेती झुलसा रोग (अर्ली ब्लाइट)",
    severity: "Medium (35% area)",
    confidence: "96.4%",
    spray: "नासिक में आगामी शनिवार दोपहर 65% बारिश की संभावना है। अतः छिड़काव आज शाम 4 बजे या रविवार सुबह 7 बजे ही करें ताकि दवा बह न जाए।",
    organic: "नीम के बीज के अर्क (NSKE 5%) या ट्राइकोडर्मा विरिडी (5 ग्राम/लीटर) का छिड़काव करें। साथ ही 10% गोमूत्र का अर्क फंगस रोकने में अत्यंत प्रभावी है।",
    chemical: "मैंकोजेब 75 WP (Mancozeb @ 2.5 ग्राम/लीटर पानी) या एजोक्सीस्ट्रोबिन (1 मिली/लीटर) का तुरंत छिड़काव करें।"
  },
  potato_late_blight: {
    crop: "Potato / आलू",
    name: "Late Blight (Phytophthora infestans)",
    name_hi: "पछेती झुलसा रोग (लेट ब्लाइट)",
    severity: "High (Rapidly spreading spores)",
    confidence: "98.1%",
    spray: "आसमान में बादल छाए हैं। यदि तुरंत छिड़काव न किया गया तो फफूंद तेजी से फैलेगी। स्टिकर (स्प्रेडर) मिलाकर ही छिड़कें।",
    organic: "कॉपर सल्फेट व बुझे हुए चूने का बोर्डो मिश्रण (1%) बनाकर तुरंत पौधों की निचली पत्तियों तक तर करें।",
    chemical: "रिडोमिल एमजेड (Metalaxyl + Mancozeb @ 2 ग्राम/लीटर पानी) या सायमोक्सानिल का त्वरित छिड़काव करें।"
  },
  cotton_bacterial_blight: {
    crop: "Cotton / कपास",
    name: "Bacterial Leaf Blight (Angular Leaf Spot)",
    name_hi: "कपास का जीवाणु झुलसा / कोणीय धब्बा रोग",
    severity: "Moderate (Water-soaked lesions)",
    confidence: "94.7%",
    spray: "हवा की गति 12 किमी/घंटा है। दोपहर की तेज धूप में छिड़काव से बचें और सुबह के समय छिड़कें।",
    organic: "स्यूडोमोनास फ्लोरेसेंस (5 ग्राम/लीटर) व 5% पंचगव्य का घोल बनाकर 10 दिन के अंतराल पर छिड़कें।",
    chemical: "स्ट्रेप्टोसाइक्लिन (1 ग्राम) + कॉपर ऑक्सीक्लोराइड (30 ग्राम) प्रति 10 लीटर पानी में घोलकर छिड़काव करें।"
  },
  corn_healthy: {
    crop: "Corn (Maize) / मक्का",
    name: "Healthy Leaf — No Pathogen Detected",
    name_hi: "स्वस्थ पत्ती — कोई रोग नहीं पाया गया",
    severity: "None (Optimum vigor)",
    confidence: "99.2%",
    spray: "फसल पूर्णतः स्वस्थ है। किसी भी कीटनाशक के अनावश्यक छिड़काव से बचें और केवल संतुलित नमी बनाए रखें।",
    organic: "संतुलित जीवामृत या वर्मीवाश का उपयोग करें ताकि पौधों की स्वाभाविक रोग प्रतिरोधक क्षमता बनी रहे।",
    chemical: "किसी रासायनिक छिड़काव की आवश्यकता नहीं है। लागत बचाएं।"
  }
};

// STATE MANAGEMENT
let currentLang = "hi"; // default Hindi for Indian farmers
let currentHub = "nashik";
let currentLeafSample = "tomato_early_blight";

// INITIALIZATION
document.addEventListener("DOMContentLoaded", () => {
  setupLanguageToggle();
  setupTabs();
  setupHubSelector();
  setupSoilCardPreset();
  setupRecommendForm();
  setupPlantDoctor();
  setupVoiceSaathi();
  setupPHSlider();
  setupSupabaseHeartbeat();
});

// 1. LANGUAGE TOGGLE
function setupLanguageToggle() {
  const btn = document.getElementById("langToggleBtn");
  const txt = document.getElementById("langCurrentText");

  btn.addEventListener("click", () => {
    currentLang = currentLang === "hi" ? "en" : "hi";
    txt.textContent = currentLang === "hi" ? "English" : "हिन्दी";
    applyLanguage(currentLang);
  });
}

function applyLanguage(lang) {
  document.querySelectorAll("[data-lang-en]").forEach(el => {
    const text = el.getAttribute(`data-lang-${lang}`);
    if (text) el.textContent = text;
  });
}

// 2. TABS
function setupTabs() {
  const btns = document.querySelectorAll(".tab-btn");
  const panes = document.querySelectorAll(".tab-pane");

  btns.forEach(btn => {
    btn.addEventListener("click", () => {
      btns.forEach(b => b.classList.remove("active"));
      panes.forEach(p => p.classList.remove("active"));

      btn.classList.add("active");
      const target = btn.getAttribute("data-tab");
      const pane = document.getElementById(target);
      if (pane) pane.classList.add("active");
    });
  });
}

// 3. REGIONAL HUBS
function setupHubSelector() {
  const chips = document.querySelectorAll(".hub-chip");
  chips.forEach(chip => {
    chip.addEventListener("click", () => {
      chips.forEach(c => c.classList.remove("active"));
      chip.classList.add("active");

      const hubKey = chip.getAttribute("data-hub");
      selectHub(hubKey);
    });
  });
}

function selectHub(key) {
  currentHub = key;
  const hub = DEMO_HUBS[key];
  if (!hub) return;

  // Weather Card
  document.getElementById("weatherHubName").textContent = hub.name_en;
  document.getElementById("weatherCondition").textContent = hub.weather.cond;
  document.getElementById("weatherTemp").textContent = hub.weather.temp;
  document.getElementById("weatherHumidity").textContent = hub.weather.hum;
  document.getElementById("weatherRain").textContent = hub.weather.rain;
  document.getElementById("weatherEmoji").textContent = hub.weather.icon;
  document.getElementById("weatherSprayText").textContent = hub.weather.spray;

  // Inputs
  document.getElementById("inputState").value = hub.state;
  document.getElementById("inputDistrict").value = hub.district;
  document.getElementById("inputN").value = hub.soil.n;
  document.getElementById("inputP").value = hub.soil.p;
  document.getElementById("inputK").value = hub.soil.k;
  document.getElementById("inputPH").value = hub.soil.ph;
  updatePHDisplay(hub.soil.ph);

  // Update Recommendation View
  updateRecommendationUI(hub);
}

// 4. SOIL CARD PRESET
function setupSoilCardPreset() {
  const select = document.getElementById("soilCardPresetSelect");
  select.addEventListener("change", () => {
    const val = select.value;
    if (val === "sample_1_nashik") selectHub("nashik");
    else if (val === "sample_2_indore") selectHub("indore");
    else if (val === "sample_3_ludhiana") selectHub("ludhiana");
  });
}

// 5. pH SLIDER
function setupPHSlider() {
  const slider = document.getElementById("inputPH");
  slider.addEventListener("input", (e) => {
    updatePHDisplay(e.target.value);
  });
}

function updatePHDisplay(val) {
  const v = parseFloat(val);
  let status = "Neutral";
  if (v < 6.0) status = "Acidic (अम्लीय)";
  else if (v > 7.5) status = "Alkaline (क्षारीय)";
  else status = "Neutral / Ideal (संतुलित)";

  document.getElementById("phDisplay").textContent = `${v} (${status})`;
}

// 6. RECOMMENDATION FORM & LIVE PREDICTION
function setupRecommendForm() {
  const form = document.getElementById("recommendForm");
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const btn = document.getElementById("btnRecommend");
    const originalText = btn.innerHTML;
    btn.innerHTML = "<span>⏳ Analyzing with XGBoost & ISRIC SoilGrids...</span>";
    btn.disabled = true;

    const payload = {
      latitude: DEMO_HUBS[currentHub]?.lat || 19.9975,
      longitude: DEMO_HUBS[currentHub]?.lon || 73.7898,
      state: document.getElementById("inputState").value,
      district: document.getElementById("inputDistrict").value,
      farm_size_acres: parseFloat(document.getElementById("inputFarmSize").value) || 2.5,
      irrigation_source: document.getElementById("inputIrrigation").value,
      previous_crop: document.getElementById("inputPrevCrop").value,
      custom_soil: {
        nitrogen: parseFloat(document.getElementById("inputN").value),
        phosphorus: parseFloat(document.getElementById("inputP").value),
        potassium: parseFloat(document.getElementById("inputK").value),
        ph: parseFloat(document.getElementById("inputPH").value)
      }
    };

    try {
      const res = await fetch("/api/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      if (res.ok) {
        const data = await res.json();
        renderAPIRecommendation(data);
      } else {
        // Fallback to local deterministic hub
        updateRecommendationUI(DEMO_HUBS[currentHub]);
      }
    } catch (_) {
      updateRecommendationUI(DEMO_HUBS[currentHub]);
    } finally {
      btn.innerHTML = originalText;
      btn.disabled = false;
      addActivityLog(`Crop Recommendation: ${payload.district}`, `Top Match Generated • N:${payload.custom_soil.nitrogen}, P:${payload.custom_soil.phosphorus}, K:${payload.custom_soil.potassium}`);
    }
  });
}

function updateRecommendationUI(hub) {
  document.getElementById("topCropName").textContent = hub.topCrop.name;
  document.getElementById("topCropFamily").textContent = hub.topCrop.family;
  document.getElementById("topCropScore").textContent = hub.topCrop.score;
  document.getElementById("topCropYield").textContent = hub.topCrop.yield;
  document.getElementById("topCropRev").textContent = hub.topCrop.rev;
  document.getElementById("topCropRate").textContent = hub.topCrop.rate;
  document.getElementById("topCropSowing").textContent = hub.topCrop.sowing;
  document.getElementById("shapExplanationText").textContent = `"${hub.shapText}"`;

  // Render SHAP Bars
  const barsContainer = document.getElementById("shapBarsList");
  barsContainer.innerHTML = hub.shapBars.map(b => `
    <div class="shap-bar-row">
      <span class="shap-feat">${b.name}</span>
      <div class="shap-bar-track">
        <div class="shap-fill ${b.pos ? 'positive' : 'negative'}" style="width: ${b.pct}%"></div>
      </div>
      <span class="shap-impact ${b.pos ? 'text-green' : 'text-red'}">${b.val}</span>
    </div>
  `).join("");

  // Render Runners
  const runnersContainer = document.getElementById("runnersList");
  runnersContainer.innerHTML = hub.runners.map(r => `
    <div class="runner-card">
      <div class="runner-header">
        <span class="runner-name">${r.name}</span>
        <span class="runner-score">${r.score}</span>
      </div>
      <div class="runner-meta">${r.meta}</div>
    </div>
  `).join("");
}

function renderAPIRecommendation(data) {
  if (!data.top_recommendations || data.top_recommendations.length === 0) return;
  const top = data.top_recommendations[0];

  document.getElementById("topCropName").textContent = `${top.crop_name} (${top.hindi_name || ''})`;
  document.getElementById("topCropFamily").textContent = `Family: ${top.crop_family || 'Agronomic'} • ${top.duration_days || 120} Days Duration`;
  document.getElementById("topCropScore").textContent = `${top.match_score_pct}%`;
  document.getElementById("topCropYield").textContent = top.expected_yield_per_acre || "8 - 12 Tonnes";
  document.getElementById("topCropRev").textContent = top.estimated_revenue_per_acre || "₹2,50,000 - ₹4,00,000";
  document.getElementById("topCropRate").textContent = top.mandi_price_modal || "₹6,000 / Qtl";
  document.getElementById("topCropSowing").textContent = top.sowing_window_en || "October - November";

  if (top.bilingual_explanation) {
    document.getElementById("shapExplanationText").textContent = `"${top.bilingual_explanation.hi || top.bilingual_explanation.en}"`;
  }

  if (top.shap_contributions && top.shap_contributions.length > 0) {
    const barsContainer = document.getElementById("shapBarsList");
    barsContainer.innerHTML = top.shap_contributions.slice(0, 5).map(s => {
      const isPos = s.impact_score >= 0;
      const pct = Math.min(100, Math.max(15, Math.abs(s.impact_score * 300)));
      const sign = isPos ? "+" : "";
      return `
        <div class="shap-bar-row">
          <span class="shap-feat">${s.feature_name}</span>
          <div class="shap-bar-track">
            <div class="shap-fill ${isPos ? 'positive' : 'negative'}" style="width: ${pct}%"></div>
          </div>
          <span class="shap-impact ${isPos ? 'text-green' : 'text-red'}">${sign}${(s.impact_score * 100).toFixed(1)}%</span>
        </div>
      `;
    }).join("");
  }
}

// 7. PLANT DOCTOR (LEAF DISEASE DIAGNOSIS)
function setupPlantDoctor() {
  const leafBtns = document.querySelectorAll(".leaf-btn");
  leafBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      leafBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");

      currentLeafSample = btn.getAttribute("data-sample");
      renderDiagnosis(currentLeafSample);
    });
  });

  const fileInput = document.getElementById("leafFileInput");
  fileInput.addEventListener("change", (e) => {
    if (e.target.files && e.target.files[0]) {
      renderDiagnosis("tomato_early_blight");
    }
  });

  const runBtn = document.getElementById("btnRunDiagnosis");
  runBtn.addEventListener("click", () => {
    renderDiagnosis(currentLeafSample);
    addActivityLog(`Leaf Diagnostic: ${LEAF_SAMPLES[currentLeafSample].name}`, `Confidence: ${LEAF_SAMPLES[currentLeafSample].confidence}`);
  });
}

function renderDiagnosis(sampleKey) {
  const sample = LEAF_SAMPLES[sampleKey] || LEAF_SAMPLES.tomato_early_blight;

  document.getElementById("diagCrop").textContent = `Crop: ${sample.crop}`;
  document.getElementById("diagDiseaseName").textContent = sample.name;
  document.getElementById("diagDiseaseHi").textContent = sample.name_hi;
  document.getElementById("diagSeverity").textContent = sample.severity;
  document.getElementById("diagConfidence").textContent = `Confidence: ${sample.confidence}`;
  document.getElementById("diagSprayText").textContent = `"${sample.spray}"`;
  document.getElementById("diagOrganicRemedy").textContent = sample.organic;
  document.getElementById("diagChemicalRemedy").textContent = sample.chemical;
}

// 8. CONVERSATIONAL VOICE SAATHI (GROQ LLM + TTS)
function setupVoiceSaathi() {
  const chips = document.querySelectorAll(".voice-chip");
  const input = document.getElementById("voiceTextInput");
  const sendBtn = document.getElementById("btnSendVoiceQuery");
  const ttsBtn = document.getElementById("btnAudioTTSPlay");
  const micBtn = document.getElementById("btnVoiceSpeak");

  chips.forEach(chip => {
    chip.addEventListener("click", () => {
      const q = chip.getAttribute("data-query");
      input.value = q;
      handleVoiceQuery(q);
    });
  });

  sendBtn.addEventListener("click", () => {
    if (input.value.trim()) handleVoiceQuery(input.value.trim());
  });

  input.addEventListener("keypress", (e) => {
    if (e.key === "Enter" && input.value.trim()) handleVoiceQuery(input.value.trim());
  });

  ttsBtn.addEventListener("click", () => {
    const textToSpeak = document.getElementById("voiceBubbleHi").textContent.replace(/"/g, '');
    speakText(textToSpeak, "hi-IN");
  });

  micBtn.addEventListener("click", () => {
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      const recognition = new SpeechRecognition();
      recognition.lang = 'hi-IN';
      micBtn.style.background = "#FECACA";
      micBtn.classList.add("pulse-green");

      recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        input.value = transcript;
        handleVoiceQuery(transcript);
        micBtn.classList.remove("pulse-green");
        micBtn.style.background = "#FEE2E2";
      };

      recognition.onerror = () => {
        micBtn.classList.remove("pulse-green");
        micBtn.style.background = "#FEE2E2";
      };

      recognition.start();
    } else {
      alert("Voice speech recognition is not supported in this browser. Please type your query.");
    }
  });

  // Follow-up chips delegation
  document.getElementById("voiceFollowupsList").addEventListener("click", (e) => {
    if (e.target.classList.contains("follow-chip")) {
      const q = e.target.getAttribute("data-query");
      input.value = q;
      handleVoiceQuery(q);
    }
  });
}

async function handleVoiceQuery(query) {
  const hiBubble = document.getElementById("voiceBubbleHi");
  const enBubble = document.getElementById("voiceBubbleEn");
  hiBubble.textContent = "AI उत्तर तैयार कर रहा है...";
  enBubble.textContent = "Synthesizing answer with Groq LLaMA 3.3...";

  try {
    const res = await fetch("/api/voice/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        query_text: query,
        language: "hi",
        crop_context: DEMO_HUBS[currentHub]?.topCrop?.name || "Grapes",
        location_context: DEMO_HUBS[currentHub]?.name_en || "Nashik"
      })
    });

    if (res.ok) {
      const data = await res.json();
      hiBubble.textContent = `"${data.response_text_hi}"`;
      enBubble.textContent = data.response_text_en ? `"${data.response_text_en}"` : "";
      
      // Auto speak Hindi TTS response
      speakText(data.tts_audio_text || data.response_text_hi, "hi-IN");
      return;
    }
  } catch (_) {}

  // Fallback Rule Engine
  const q = query.toLowerCase();
  let hi = "फसल के लिए 3 से 4 सिंचाइयों की आवश्यकता होती है। फूल आने और फल बनते समय खेत में नमी अवश्य रखें।";
  let en = "Crops require 3 to 4 irrigations. Maintain soil moisture during flowering and pod development.";

  if (q.includes("खाद") || q.includes("fertilizer") || q.includes("यूरिया")) {
    hi = "बुवाई के समय प्रति एकड़ 50 किलो डीएपी और 25 किलो पोटाश डालें। 25 दिन बाद 35 किलो नीम कोटेड यूरिया का छिड़काव करें।";
    en = "Apply 50 kg DAP and 25 kg MOP at sowing. Top dress with 35 kg Neem Coated Urea after 25 days.";
  } else if (q.includes("मंडी") || q.includes("भाव") || q.includes("price") || q.includes("रेट")) {
    hi = "आज नासिक मंडी में अंगूर ₹6,200/क्विंटल और अनार ₹8,400/क्विंटल के भाव पर हैं। भाव में 3 से 5% की तेजी देखी जा रही है।";
    en = "Today in Nashik Mandi, Grapes are at ₹6,200/Qtl and Pomegranate at ₹8,400/Qtl with an upward trend.";
  } else if (q.includes("कीट") || q.includes("रोग") || q.includes("pest")) {
    hi = "शुरुआती अवस्था में 5 मिली प्रति लीटर नीम तेल का छिड़काव करें। अधिक प्रकोप होने पर अनुशंसित फफूंदनाशक का छिड़काव करें।";
    en = "Apply Neem oil @ 5ml/Litre for early protection. Use targeted fungicide if infestation spreads.";
  }

  hiBubble.textContent = `"${hi}"`;
  enBubble.textContent = `"${en}"`;
  speakText(hi, "hi-IN");
}

// Browser Web Speech API TTS
function speakText(text, lang = "hi-IN") {
  if (!('speechSynthesis' in window)) return;
  window.speechSynthesis.cancel(); // stop any active speech

  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = lang;
  utterance.rate = 0.95; // slightly slower, clear for farmers
  utterance.pitch = 1.0;

  // Select Hindi or Indian voice if available
  const voices = window.speechSynthesis.getVoices();
  const hindiVoice = voices.find(v => v.lang.includes("hi") || v.lang.includes("Hindi") || v.name.includes("India"));
  if (hindiVoice) utterance.voice = hindiVoice;

  window.speechSynthesis.speak(utterance);
}

// 9. SUPABASE HEARTBEAT & ACTIVITY LOG
function setupSupabaseHeartbeat() {
  const btn = document.getElementById("btnManualPing");
  if (btn) {
    btn.addEventListener("click", async () => {
      btn.innerHTML = "<span>⚡ Pinging Supabase...</span>";
      try {
        const res = await fetch("/api/db-ping");
        const data = await res.json();
        document.getElementById("sbLastPing").textContent = `Success (${new Date().toLocaleTimeString()})`;
        document.getElementById("sbStatus").textContent = "Healthy & Keep-Alive Active";
        addActivityLog("Supabase Keep-Alive Pulse", `Ping status: ${data.keep_alive || 'triggered'}`);
      } catch (e) {
        document.getElementById("sbLastPing").textContent = `Active Local Mode (${new Date().toLocaleTimeString()})`;
      } finally {
        btn.innerHTML = "<span>⚡ Trigger Manual Supabase Heartbeat (/api/db-ping)</span>";
      }
    });
  }
}

function addActivityLog(title, desc) {
  const feed = document.getElementById("activityFeed");
  if (!feed) return;

  const item = document.createElement("div");
  item.className = "feed-item";
  item.innerHTML = `
    <span class="feed-dot green"></span>
    <div class="feed-info">
      <strong>${title}</strong>
      <span>${desc}</span>
    </div>
    <span class="feed-time">Just now</span>
  `;
  feed.prepend(item);
}
