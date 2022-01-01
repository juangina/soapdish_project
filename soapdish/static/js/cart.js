//console.log('cart.js implemented');

var updateBtns = document.getElementsByClassName('update-cart')
var deleteBtns = document.getElementsByClassName('delete-item')
var updateSelection = document.getElementsByClassName('item-quantity')
var itemQty = document.getElementById('itemQty')


for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		var itemQty = document.getElementById('itemQty');
		if(itemQty) {
			var qty = itemQty.value;
		}
		else {
			var qty = 1
		}
		console.log(productId, action, qty);

		//console.log('productId:', productId, 'Action:', action)
		//console.log('USER:', user)

		if (user == 'AnonymousUser'){
			addCookieItem(productId, action, qty);
		}else{
			updateUserOrder(productId, action, qty);
		}
	})
}

for (i = 0; i < updateBtns.length; i++) {
	var productQty = updateBtns[i].dataset.qty
	//console.log(productQty);
	if(productQty <= 0) {
		updateBtns[i].disabled = true;
		if(itemQty) {
			itemQty.disabled = true;
		}
		updateBtns[i].innerHTML = "Out of Stock!";
	}
	//console.log(updateBtns[i]);
}

for (i = 0; i < deleteBtns.length; i++) {
	deleteBtns[i].addEventListener('click', function() {
		var productId = this.dataset.product;
		var action = this.dataset.action;
		var qty = '1';
		console.log(productId, action, qty);

		if (user == 'AnonymousUser'){
			addCookieItem(productId, action, qty);
		}else{
			updateUserOrder(productId, action, qty);
		}		
	})
}
for (i = 0; i < updateSelection.length; i++) {
	updateSelection[i].addEventListener('change', function(e) {
		var productId = this.dataset.product;
		var action = this.dataset.action;
		var qty = e.target.value;
		console.log(productId, action, qty);

		if (user == 'AnonymousUser'){
			addCookieItem(productId, action, qty);
		}else{
			updateUserOrder(productId, action, qty);
		}
	})
}

function updateUserOrder(productId, action, qty){
	//console.log('User is authenticated, sending data...')
	
	var url = '/store/update_item/'

	fetch(url, {
		method:'POST',
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,
		}, 
		body:JSON.stringify({'productId':productId, 'action':action, 'qty':qty})
	})
	.then((response) => {
		return response.json();
	})
	.then((data) => {
		location.reload()
	});
	
	//console.log('Item Quantity: ' + qty);	
}

function addCookieItem(productId, action, qty){
	//console.log('User is not authenticated')
	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity': parseInt(qty)}

		}else{
			cart[productId]['quantity'] += parseInt(qty)
		}
	}
	else if (action == 'add1'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity':1}

		}else{
			cart[productId]['quantity'] += 1
		}
	}
	else if (action == 'remove1'){
		if (cart[productId]['quantity'] > 1) {
			cart[productId]['quantity'] -= 1
		}
		
		if (cart[productId]['quantity'] <= 0){
			delete cart[productId];
		}
	}
	else if (action == 'delete') {
		delete cart[productId];
	}
	//console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()
}