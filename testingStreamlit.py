import streamlit as st

#Basic Text Elements
st.title(":red[It is the title]")
st.header("🕵🏻‍♀️ this is the header")
st.subheader("this is the subheader")
st.text("this is text")
st.write("this is write")
st.caption("caption")

#Displaying Code
code_sample="""
def display():
    print("hello")
"""
st.code(code_sample)

# widgets/inputs
location=st.selectbox("choose your location",['nainital','haldwani'])
st.write(f"{location}")
st.success(f"{location}")

btn=st.button("click me")
st.write(btn)

chk=st.checkbox("remember me")
st.write(chk)

text=st.text_input("username")
st.write(text)
print(type(text))
fedbck=st.text_area("feedbCK")
st.write(fedbck)

nmbr=st.number_input("AGE")
st.write(nmbr)

people = st.number_input("How many people", min_value=1, max_value=10, step=1)
st.write(f"{people}")

dob = st.date_input("Select your date of birth",format= "DD/MM/YYYY")
st.write(f"Your date of birth {dob}")

Gender = st.radio("Gender: ", ["Male", "Female", "Almond Other"])
st.write(f"{Gender}")

value=st.slider("select range ",1,100,10)
st.write(value)

city_prefer=st.multiselect("choose city ",["Dehradun","Delhi","Mumbai","Jaipur"])
st.write(city_prefer)

upload=st.file_uploader("upload file ")
st.write(upload)

#fomr
with st.form("Enquiry"):
    name=st.text_input("Name")
    age=st.text_input("age")
    submit=st.form_submit_button("submit")

#columns or layout
col1,col2=st.columns(2,border=True)
with col1:
    st.text("Name")
    

with col2:
    st.text("Age")


#expander
with st.expander("Your QUestion"):
    st.write('''
        Answer
    ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")

#sidebar
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

#chat element
with st.chat_message("user"):
    st.write("Hello 👋")

prompt = st.chat_input(
    "Say something and/or attach an image",
    accept_file=True,
    file_type=["jpg", "jpeg", "png"],
)
if prompt and prompt.text:
    st.markdown(prompt.text)
if prompt and prompt["files"]:
    st.image(prompt["files"][0])