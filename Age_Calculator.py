import streamlit as st
import datetime

st.title("🎯 Age Calculator")

# Date input for user date of birth
min_date = datetime.date(2000, 1, 1)
max_date = datetime.date(2100, 12, 31)
default_date = datetime.date.today()
dob = st.date_input("Enter your date of birth:", value=default_date, min_value=min_date, max_value=max_date, key=None)

# Calculate age button
if st.button("Calculate Age"):
    today = datetime.date.today()

    if dob > today:
        st.error("❌ Date of birth cannot be in the future!")
    else:
        age_years = today.year - dob.year
        age_months = today.month - dob.month
        age_days = today.day - dob.day

        # Adjust if current month/day is smaller than dob
        if age_days < 0:
            age_months -= 1
            age_days += 30
        if age_months < 0:
            age_years -= 1
            age_months += 12

        st.success(f"🎉 Your Age is:  \n **{age_years} years, {age_months} months, {age_days} days**")

st.write("---")
st.write("Enter your DOB above and click the button to calculate your age 😉")
