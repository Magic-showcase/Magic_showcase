
  paypal.Buttons({
    createOrder: function(data, actions) {
      // This function sets up the details of the transaction, including the amount and line item details.
      return actions.order.create({
        purchase_units: [{
          amount: {
            value: '300'
          }
        }]
      });
    },
    onApprove: function(data) {
      return fetch('/pago/', {
        method: 'POSOT',
        headers: {
          'content-type': 'application/json',
          'X-CSRFToken': csrftoken,

        },
        body: JSON.stringify({
          orderID: data.orderID
        })
      }).then(function(res) {
        return res.json();
      }).then(function(details) {
        alert('Transaction approved by ' + details.payer_given_name);
    
    })
  }

  }).render('#paypal-button-container');
  //This function displays Smart Payment Buttons on your web page.
