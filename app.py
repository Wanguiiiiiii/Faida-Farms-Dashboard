import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="Faida Farms — FMNR Baseline System",
    page_icon="🌱",
    layout="wide"
)

# 2. Inject Visual CSS Theme 
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ------------------------------------------------------------------
# STATIC PROTOTYPE MOCK DATA 
# ------------------------------------------------------------------
roster_data = pd.DataFrame({
    "Enumerator Name": ["John Koech", "Mary Mwangi", "David Lekuta", "Grace Mutua"],
    "Assigned Site/County": ["Osiligi Cluster (Kajiado)", "Kalawa Sector (Makueni)", "Mara Node (Narok)", "Kitise/Twaandu (Makueni)"],
    "Respondents Interacted": [34, 45, 28, 35],
    "Target Household Goal": [40, 40, 40, 40],
    "Progress Status": ["85.0% Complete", "100% Finalized", "70.0% Complete", "87.5% Complete"]
})

# ------------------------------------------------------------------
# SIDEBAR NAVIGATION
# ------------------------------------------------------------------
with st.sidebar:
    st.markdown("""
        <div style='text-align: center; margin-bottom:10px;'>
            <h1 style='font-size: 28px; margin:0; color:#FF6B00;'>🌱 FAIDA FARMS</h1>
            <h5 style='color:#FFF; margin:0; font-size:11px; letter-spacing:1px;'>FMNR INTERPRETATION ENGINE</h5>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    
    # Clean Profiles Setup
    st.markdown("👤 **Select Active Dashboard Profile:**")
    user_profile = st.selectbox(
        "Select User Profile:",
        ["Field Enumerator", "M&E Supervisor / Manager", "Executive / Director"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.caption("System Status: Operational\nResearch Framework: World Vision GREEN Project Baseline\nRegion: Makueni, Kajiado, Narok")

# ------------------------------------------------------------------
# FAIDA FARMS MASTER BANNER
# ------------------------------------------------------------------
st.markdown("""
    <div class="hero-banner">
        <h3>🌱 FAIDA FARMS SYSTEMS</h3>
        <h1>FARMER MANAGED NATURAL REGENERATION (FMNR) PROJECT DASHBOARD</h1>
        <div style="color: #666; font-weight: 600;">Evaluating Landscape Restoration for Household Resilience, Food Security & Child Well-being in Kenya's ASALs</div>
    </div>
""", unsafe_allow_html=True)


# ==================================================================
# PROFILE 1: FIELD ENUMERATOR DASHBOARD VIEW
# ==================================================================
if user_profile == "Field Enumerator":
    st.markdown("### 📋 My Personal Field Tracker (Enumerator Interface)")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("<div class='section-title'>📊 Target Collection Milestones</div>", unsafe_allow_html=True)
        e1, e2, e3 = st.columns(3)
        e1.metric(label="RESPONDENTS INTERACTED WITH", value="45 Households", delta="Daily Target Reached")
        e2.metric(label="MY RUNNING PROGRESS INDICATOR", value="100%", delta="Completed")
        e3.metric(label="LAST SURVEY AREA COVERED", value="Makueni (Kalawa Sector)", delta="GPS Coordinate Lock OK")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.info("💡 **Field Device Tip:** Visual interface environment is operational. Toggle metrics to review active evaluation modules.")

    with col2:
        st.markdown("<div class='section-title'>🗺️ Active Survey Segment Mapping</div>", unsafe_allow_html=True)
        st.markdown("""
            <div class='species-card'>
                <div class='species-title'>📍 Allocated Spatial Node</div>
                <p class='species-meta'>
                    <b>Active Evaluation Tool:</b> Tool 1 - Screening & Identification Form<br>
                    <b>Target Cluster Node:</b> Kalawa Sub-location Treatment Households<br>
                    <b>Status:</b> Verification Active
                </p>
            </div>
        """, unsafe_allow_html=True)


# ==================================================================
# PROFILE 2: M&E SUPERVISOR / MANAGER DASHBOARD VIEW
# ==================================================================
elif user_profile == "M&E Supervisor / Manager":
    st.markdown("### 🛠️ Operations Oversight & Research Management Control Window")
    
    st.markdown("<div class='section-title'>📈 Aggregate Research Field Performance</div>", unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    m1.metric(label="TOTAL COMPLETED INTERVIEWS", value="142 / 160 Submissions", delta="88.7% Global Progress")
    m2.metric(label="ACTIVE RECRUITED FIELD ENUMERATORS", value="4 Research Officers", delta="All Active")
    m3.metric(label="MAPPED TARGET COMMUNITIES", value="3 Counties Active", delta="Makueni, Kajiado, Narok")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Enumerator Matrix Tracking
    st.markdown("<div class='section-title'>👥 Individual Enumerator Progress Real-Time Matrix</div>", unsafe_allow_html=True)
    st.dataframe(roster_data, width=None, hide_index=True)


# ==================================================================
# PROFILE 3: EXECUTIVE / DIRECTOR DASHBOARD VIEW
# ==================================================================
elif user_profile == "Executive / Director":
    st.markdown("### 👑 Enterprise Strategic Impact & Executive Oversight Center")
    
    st.markdown("<div class='section-title'>🦅 FMNR Approved Evaluation Domains Overview</div>", unsafe_allow_html=True)
    ex1, ex2, ex3 = st.columns(3)
    ex1.metric(label="HOUSEHOLD RESILIENCE STUDY POOL", value="142 Households Evaluated", delta="Makueni, Kajiado, Narok")
    ex2.metric(label="CHILD WELL-BEING TARGET AUDIT DATA", value="99.4% Complete", delta="Under-5 Dietary Tracking Intact")
    ex3.metric(label="FMNR COHORT DISTRIBUTION MIX", value="85 Intervention / 57 Control", delta="Quasi-Experimental Design Split")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    left_don, right_don = st.columns([1.5, 1])
    with left_don:
        st.markdown("#### 📸 Social Context Monitoring: Livelihoods & Children Support")
        st.markdown("""
            The **Faida Farms Dashboard** processes core structural metrics defined by the baseline protocol. 
            Early descriptive trends indicate a strong baseline nexus between active farmer adoption parameters and 
            resilient household dietary diversity access margins throughout the focal semi-arid locations.
        """)
        
        img_col1, img_col2 = st.columns(2)
        with img_col1:
            st.image("https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?auto=format&fit=crop&q=80&w=500", 
                     caption="Evaluating structural dietary diversity interventions and field nutrition distribution safety channels.")
        with img_col2:
            st.image("https://images.unsplash.com/photo-1542810634-71277d95dcbb?auto=format&fit=crop&q=80&w=500", 
                     caption="Monitoring health parameters and child performance indicators inside designated research nodes.")

    with right_don:
        st.markdown("#### 🪵 Core Measured Research Domain Status")
        st.markdown("""
            <div class="species-card" style="border-left: 4px solid #34A853;">
                <div class="species-title">Domain 1 & 2: FMNR Intensity & Resilience Index</div>
                <p class="species-meta">Tracking plot observation scores, shock exposure parameters, adaptive capacities, and asset structures across treatment cohorts.</p>
            </div>
            <div class="species-card" style="border-left: 4px solid #FF6B00;">
                <div class="species-title">Domain 3 & 4: Food Security & Dietary Diversity Indices</div>
                <p class="species-meta">Evaluating HFIAS parameters, MAHFP scales, and 24-hour child dietary diversity food-group consumption scores.</p>
            </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div style='text-align: center; color: #999; font-size:12px;'>© World Vision Kenya GREEN Project — Faida Farms Monitoring Frame</div>", unsafe_allow_html=True)