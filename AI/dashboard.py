import plotly.express as px 


def plot_payment_dashboard(data):
    fig=px.bar(data, x='User', y='Amount', title='Payments Dashboard')
    dif.show()