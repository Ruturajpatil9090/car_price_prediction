from nturl2path import url2pathname
from os import urandom
import streamlit as st
import pickle
model =pickle.load(open('model.pkl','rb'))

def main():
    string = "Car price Predictor"
    st.title("Car price Predictor")
    st.markdown("Are you selling your car?")
    # st.image(
    #        "https://pixabay.com/photos/auto-automobile-automotive-amg-2179220",
    #         width=500, 
    # )

    st.write('')
    st.write('')

    year = st.number_input("In which year car was purchased :",1990,2022,step=1,key = 'year')
    year_old = 2022-year

    Present_Price = st.number_input("what is the ex-showrrom price of car(ln ₹lakhs) :",0.00,50.00,step=0.5,key='present_price')

    km_driven =st.number_input('Distance completed by car(in km):',0.00,500000.00,step=500.00,key='drived')

    owner = st.radio("The number of owners :",(0,1,3),key='owner')

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
            prediction = Model.predict([[Present_Price, km_driven, owner, year_old, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]])
            output = round(prediction[0],2)
            if output<0:
                st.warning("You will be not able to sell this car !!")
            else:
                st.success("You can sell the car for {} lakhs 🙌".format(output))
        except:
            st.warning("Opps!! Something went wrong\nTry again")



if __name__ == '__main__':
    main()

