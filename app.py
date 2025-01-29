# importing required libraries
import pandas as pd
import pickle
import gradio as gr


# creating function for interface
def interface(income,age,score):
    df=pd.DataFrame({'Yearly_Income':[income],'Age':[age],'Cust_Spend_Score':[score]})
    model=pickle.load(open('model creation/customer_cluster.pkl','rb'))
    pred = model.predict(df)
    dic={0:'mean salary is 78370 , mean age is 36 and mean score is 50',1:'mean salary is 42230 , mean age is 43 and mean score is 51',2:'mean salary is 1,05,300 , mean age is 37 and mean score is 53',3:'mean salary is 22,000 , mean age is 34 and mean score is 51',4:'mean salary is 60,440  , mean age is 42 and mean score is 51'}
    return  (f'customer belongs to the category where  {dic[pred[0]]} ')

# creating the interface
interface=gr.Interface(fn=interface,
                       inputs=[gr.components.Number(label='Enter income here...'),gr.components.Number(label='Enter age here...'),gr.components.Number(label='Enter  Customer Spend Score here...')],
                   outputs='text',
                   theme='freddyaboulton/test-blue')
# launching the interface
interface.launch()

