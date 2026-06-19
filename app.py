import streamlit as st
import os

from extractor import extract_text
from ddr_generator import generate_ddr
from report_export import create_docx

st.set_page_config(page_title="DDR Report Generator")

st.title("🏢 DDR Report Generator")

inspection_file = st.file_uploader(
    "Upload Inspection Report",
    type=["pdf"],
    key="inspection"
)

thermal_file = st.file_uploader(
    "Upload Thermal Report",
    type=["pdf"],
    key="thermal"
)

if st.button("Generate DDR"):

    if inspection_file and thermal_file:

        os.makedirs("uploads", exist_ok=True)

        inspection_path = f"uploads/{inspection_file.name}"
        thermal_path = f"uploads/{thermal_file.name}"

        with open(inspection_path, "wb") as f:
            f.write(inspection_file.getbuffer())

        with open(thermal_path, "wb") as f:
            f.write(thermal_file.getbuffer())

        inspection_text = extract_text(inspection_path)
        thermal_text = extract_text(thermal_path)

        ddr_report = generate_ddr(
            inspection_text,
            thermal_text
        )

        doc_file = create_docx(ddr_report)

        st.success("DDR Generated Successfully!")

        st.subheader("Inspection Report Preview")
        st.write(inspection_text[:1000])

        st.subheader("Thermal Report Preview")
        st.write(thermal_text[:1000])

        st.subheader("Generated DDR Report")

        st.text_area(
            "DDR Output",
            ddr_report,
            height=500
        )

        with open(doc_file, "rb") as file:

            st.download_button(
                label="📄 Download DDR Report",
                data=file,
                file_name="DDR_Report.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

    else:
        st.error("Please upload both PDFs.")

