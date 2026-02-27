def run_system(ehr_text, patient_sequence,
               reasoner):

    result = reasoner.analyze(
        ehr_text,
        patient_sequence
    )

    print("=== SAFETY REPORT ===")
    for k, v in result.items():
        print(k, ":", v)
