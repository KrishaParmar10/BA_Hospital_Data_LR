if st.button('Predict Hospital Total Cost'):
    input_data = np.array([[
        TOTAL_AMOUNT_BILLED_TO_THE_PATIENT,
        CONCESSION,
        ACTUAL_RECEIVABLE_AMOUNT,
        TOTAL_LENGTH_OF_STAY,
        LENGTH_OF_STAY_ICU,
        LENGTH_OF_STAY_WARD,
        COST_OF_IMPLANT
    ]])

    st.write("Input shape:", input_data.shape)
    st.write("Model expects:", model.n_features_in_)

    try:
        prediction = model.predict(input_data)[0]
        st.success(f'Predicted Hospital Cost: {prediction:.2f}')
    except Exception as e:
        st.error(f"Prediction error: {e}")






