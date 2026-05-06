import streamlit as st

st.set_page_config(
    page_title="Sandhya Aqua - Daily Feed Calculator",
    layout="wide",
)


def inject_theme() -> None:
    st.markdown(
        """
        <style>
            .stApp {
                background: linear-gradient(180deg, #EAF1FB 0%, #DCE7F8 100%);
            }

            .block-container {
                background: rgba(255, 255, 255, 0.90);
                border-radius: 14px;
                padding: 2rem 2.2rem 1.8rem 2.2rem;
                box-shadow: 0 10px 28px rgba(30, 58, 138, 0.12);
                max-width: 96% !important;
                min-height: calc(100vh - 4rem);
                border: 1px solid #D8E2F3;
            }

            h1 {
                color: #0F172A;
                font-size: 2.3rem !important;
                font-weight: 700;
            }

            h3 {
                color: #1F2937;
                font-size: 1.45rem !important;
            }

            label, p, div {
                color: #1F2937;
            }

            [data-testid="stNumberInput"] label {
                color: #1F2937 !important;
                font-size: 1.05rem !important;
                font-weight: 600;
            }

            [data-testid="stNumberInput"] input {
                color: #0F172A !important;
                font-size: 1.05rem !important;
                background: #F8FBFF !important;
                border: 1px solid #B9CAE8 !important;
                border-radius: 10px !important;
            }

            .stButton > button {
                background: #BFDBFE !important;
                color: #123B7A !important;
                border: 1px solid #93C5FD !important;
                border-radius: 10px !important;
                font-weight: 700 !important;
                font-size: 1.08rem !important;
                padding: 0.58rem 1rem !important;
            }

            .stButton > button:hover {
                background: #93C5FD !important;
                color: #0C2F66 !important;
            }

            [data-testid="stMetricLabel"] p {
                font-size: 1.02rem !important;
                font-weight: 600 !important;
            }

            [data-testid="stMetricValue"] {
                font-size: 1.85rem !important;
                color: #123B7A !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def validate_inputs(pop, surv, adg, protein, digest, prod):
    errors = []

    if pop <= 0:
        errors.append("Population must be > 0")
    if not (0 < surv <= 100):
        errors.append("Survival must be between 0-100")
    if adg <= 0:
        errors.append("ADG must be > 0")
    if not (0 < protein <= 100):
        errors.append("Feed Protein must be 0-100")
    if not (0 < digest <= 100):
        errors.append("Digestibility must be 0-100")
    if prod < 0:
        errors.append("Productivity cannot be negative")

    return errors


def calculate(pop, surv, adg, protein, digest, prod):
    NPU = 0.5

    population = pop * 1_000_000
    survival = surv / 100
    productivity = prod / 100

    biomass = (population * survival * adg) / 1000
    protein_inc = biomass * 0.21
    dig_protein = protein * (digest / 100)

    daily_feed = protein_inc / ((dig_protein * NPU) / 100)
    fcr = daily_feed / biomass
    corrected_fcr = fcr - (fcr * productivity)

    return daily_feed, corrected_fcr


def main():
    inject_theme()

    st.title("Sandhya Aqua - Daily Feed Calculator")
    st.markdown("### Input Parameters")

    col1, col2 = st.columns(2)

    with col1:
        pop = st.number_input("Population (in millions)", value=1.0)
        surv = st.number_input("Survival (%)", value=100.0)
        adg = st.number_input("Est ADG (g)", value=0.3)

    with col2:
        protein = st.number_input("Feed Protein (%)", value=37.0)
        digest = st.number_input("Digestibility (%)", value=90.0)
        prod = st.number_input("Natural Productivity (%)", value=10.0)

    if st.button("Calculate Feed"):
        errors = validate_inputs(pop, surv, adg, protein, digest, prod)

        if errors:
            for error in errors:
                st.warning(error)
        else:
            daily_feed, corrected_fcr = calculate(pop, surv, adg, protein, digest, prod)

            st.markdown("### Results")
            result_col1, result_col2 = st.columns(2)
            result_col1.metric("Estimated Daily Feed (Kg)", f"{daily_feed / 10:.1f}")
            result_col2.metric("Corrected FCR", f"{corrected_fcr:.2f}")

    st.markdown("---")
    st.caption("Developed for Sandhya Aqua")


if __name__ == "__main__":
    main()
