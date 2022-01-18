checkoutPage = document.getElementById('cart-summary-checkout')
if(checkoutPage) {
    var total = '{{order.get_checkout_total}}'
    // Render the PayPal button into #paypal-button-container
    paypal.Buttons(
        {
            //Object to Style the paypal button experience
            style: {
                color:  'blue',
                shape:  'rect',
            },
    
            // onInit is called when the button first renders
            onInit: function(data, actions) {
    
                ///////////////// Disable the buttons
                //console.log("Disable Paypal Buttons...")
                actions.disable();
    
                //////////////// Listen for user to press shipping
                document.querySelector('#shipping-form-button')
                .addEventListener('click', function(e) {
                    //console.log("Enable Paypal Buttons...")
                    actions.enable();
                });
            },
    
            //Callback to Set up the transaction
            createOrder: function(data, actions) {
            //////////////////////////////////////
                return actions.order.create({
                /////////////////////////////	
                    purchase_units: [{
                    //////////////////
                        amount: {
                        /////////
                            value:parseFloat(total).toFixed(2)
                        /////////
                        }
                    //////////////////
                    }]
                ////////////////////////////
                });
            //////////////////////////////////////
            },
    
            //Callback to Finalize the transaction
            onApprove: function(data, actions) {
                return actions.order.capture().then(function(orderData) {
                    console.log('Capture Result', orderData, JSON.stringify(orderData, null,2));
                    var transaction = orderData.purchase_units[0].payments.captures[0];
                    console.log('Transaction ' + transaction.status + ': ' + transaction.id)
    
                    // Send data from paypal to Soapdish backend server
                    submitFormData()
                    //actions.redirect('thank_you.html')
                });
            }
        }
    ).render('#paypal-button-container');
    
    var userForm = document.getElementById('user-form')
    var billingForm = document.getElementById('billing-form')
    var shippingForm = document.getElementById('shipping-form')
    var purchaseForm = document.getElementById('purchase-form')
    
    var shipping = '{{order.shipping}}'
    
    userForm.addEventListener('submit', function(e){
            e.preventDefault()
            console.log('User Form Submitted...')
            document.getElementById('user-information').innerHTML = "Done:  User Information"
            document.getElementById('user-form-button').classList.add("hidden");
            document.getElementById('billing-information').innerHTML = "Step Two:  Verify and Complete Billing Address"
            document.getElementById("billing-information-fieldset").disabled = false;
            document.getElementById('billing-form-button').classList.remove("hidden");
        }
    )
    
    billingForm.addEventListener('submit', function(e){
            e.preventDefault()
            console.log('Billing Form Submitted...')
            document.getElementById('billing-information').innerHTML = "Done:  Billing Information"
            document.getElementById('billing-form-button').classList.add("hidden");
            document.getElementById('shipping-information').innerHTML = "Verify and Complete Shipping Method"
            document.getElementById("shipping-information-fieldset").disabled = false;
            document.getElementById('shipping-form-button').classList.remove("hidden");
        }
    )
    
    shippingForm.addEventListener('submit', function(e){
            e.preventDefault()
            console.log('Shipping Form Submitted...')
            document.getElementById('shipping-information').innerHTML = "Done:  Shipping Information"
            document.getElementById('shipping-form-button').classList.add("hidden");
            document.getElementById('purchase-information').innerHTML = "Review and Complete Your Payment!"
        }
    )
    
    function submitFormData(){
        //console.log('Payment button clicked')
        //Create a JS type Form for submitting to Soapdish Store API
        var userFormData = {
            'name':null,
            'email':null,
            'total':total,
        }
    
        var billingInfo = {
            'address':null,
            'city':null,
            'state':null,
            'zipcode':null,
        }
    
    
        userFormData.name = userForm.name.value
        userFormData.email = userForm.email.value
    
        billingInfo.address = billingForm.address.value
        billingInfo.city = billingForm.city.value
        billingInfo.state = billingForm.state.value
        billingInfo.zipcode = billingForm.zipcode.value
    
        //console.log('Shipping Info:', shippingInfo)
        //console.log('User Info:', userFormData)
    
        //Send process results to 'backend' for database storage
        var url = "/store/process_order/"
        fetch(url, {
            method:'POST',
            headers:{
                'Content-Type':'applicaiton/json',
                'X-CSRFToken':csrftoken,
            }, 
            body:JSON.stringify({'form':userFormData, 'billing':billingInfo}),
            
        })
        .then((response) => response.json())
        .then((data) => {
            //console.log('Success:', data);
            alert('Transaction completed');  
    
            cart = {}
            document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
    
            window.location.href = "{% url 'store' %}"
    
            })
    }
}

