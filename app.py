import streamlit as st
import pickle
model = pickle.load(open('RF_price_predicting_model.pkl','rb'))

def main():
    string = "shubham project"
    st.set_page_config(page_title=string, page_icon="🚗") 
    st.markdown("<h1 style='text-align: center; color: Black;'>Car Bazar 🚗</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: grey;'>Sell your car at True value </h2>", unsafe_allow_html=True)
    st.markdown("##### Are you planning to sell your car !? Perfect way to buy ad sell your car in our platform.. 🤖 ")
    st.image(
            "https://www.best-selling-cars.com/wp-content/uploads/2021/01/Volkswagen-USA-Lineup.jpg",
            width=600, # Manually Adjust the width of the image as per requirement
        )
    st.write('')
    st.write('')
    years = st.number_input('In which year car was purchased ?',1990, 2021, step=1, key ='year')
    Years_old = 2021-years

    Present_Price = st.number_input('What is the current ex-showroom price of the car ?  (In ₹lakhs)', 0.00, 50.00, step=0.5, key ='present_price')

    Kms_Driven = st.number_input('What is distance completed by the car in Kilometers ?', 0.00, 500000.00, step=500.00, key ='drived')

    Owner = st.radio("The number of owners the car had previously ?", (0, 1, 3), key='owner')

    Fuel_Type_Petrol = st.selectbox('What is the fuel type of the car ?',('Petrol','Diesel', 'CNG'), key='fuel')
    if(Fuel_Type_Petrol=='Petrol'):
        Fuel_Type_Petrol=1
        Fuel_Type_Diesel=0
    elif(Fuel_Type_Petrol=='Diesel'):
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1
    else:
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=0

    Seller_Type_Individual = st.selectbox('Are you a dealer or an individual ?', ('Dealer','Individual'), key='dealer')
    if(Seller_Type_Individual=='Individual'):
        Seller_Type_Individual=1
    else:
        Seller_Type_Individual=0	

    Transmission_Mannual = st.selectbox('What is the Transmission Type ?', ('Manual','Automatic'), key='manual')
    if(Transmission_Mannual=='Mannual'):
        Transmission_Mannual=1
    else:
        Transmission_Mannual=0

    if st.button("Estimate Price", key='predict'):
        try:
            Model = model  #get_model()
            prediction = Model.predict([[Present_Price, Kms_Driven, Owner, Years_old, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]])
            output = round(prediction[0],2)
            if output<0:
                st.warning("You will be not able to sell this car !!")
            else:
                st.success("You can sell the car for {} lakhs 🙌".format(output))
        except:
            st.warning("Opps!! Something went wrong\nTry again")

if __name__ == '__main__':
    main()
