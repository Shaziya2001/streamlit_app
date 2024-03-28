import streamlit as st

def ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level):
    # Calculate conversion rates for control and treatment groups
    control_conversion_rate = control_conversions / control_visitors
    treatment_conversion_rate = treatment_conversions / treatment_visitors
    
    # Calculate pooled probability
    pooled_probability = (control_conversions + treatment_conversions) / (control_visitors + treatment_visitors)
    
    # Calculate pooled standard error
    pooled_standard_error = (pooled_probability * (1 - pooled_probability) * ((1 / control_visitors) + (1 / treatment_visitors))) ** 0.5
    
    # Calculate z-score based on confidence level
    if confidence_level == 90:
        z_score = 1.645
    elif confidence_level == 95:
        z_score = 1.96
    elif confidence_level == 99:
        z_score = 2.576
    else:
        raise ValueError("Confidence level must be 90, 95, or 99")
    
    # Calculate margin of error
    margin_of_error = z_score * pooled_standard_error
    
    # Calculate difference in conversion rates
    difference = treatment_conversion_rate - control_conversion_rate
    
    # Perform hypothesis test
    if difference > margin_of_error:
        return "Treatment Group is Better"
    elif difference < -margin_of_error:
        return "Control Group is Better"
    else:
        return "Indeterminate"
# Streamlit app layout
st.title('A/B Test Hypothesis Test')
st.write('This app performs an A/B test and determines whether the experiment group is better, the control group is better, or if the result is indeterminate.')

control_visitors = st.number_input('Enter the number of visitors in the control group:')
control_conversions = st.number_input('Enter the number of conversions in the control group:')
treatment_visitors = st.number_input('Enter the number of visitors in the treatment group:')
treatment_conversions = st.number_input('Enter the number of conversions in the treatment group:')
confidence_level = st.selectbox('Select the confidence level:', [90, 95, 99])

if st.button('Run Hypothesis Test'):
    result = ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level)
    st.write('Result:', result)
