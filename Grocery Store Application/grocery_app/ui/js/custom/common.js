var productListApiUrl = 'http://127.0.0.1:5000/getProducts';
var uomListApiUrl = 'http://127.0.0.1:5000/getUOM';
var productSaveApiUrl = 'http://127.0.0.1:5000/insertProduct';
var productDeleteApiUrl = 'http://127.0.0.1:5000/deleteProduct';
var orderListApiUrl = 'http://127.0.0.1:5000/getAllOrders';
var orderSaveApiUrl = 'http://127.0.0.1:5000/insertOrder';

// For product drop in order
var productsApiUrl = 'https://fakestoreapi.com/products';
// Helper function to make API calls using Axios
async function callApi(method, url, data) {
    try {
        const response = await axios({
            method: method,
            url: url,
            data: data
        });
        window.location.reload();
    } catch (error) {
        console.error('Error:', error);
    }
}

function calculateValue() {
    var total = 0;
    var productItems = document.querySelectorAll('.product-item');
    productItems.forEach(function (item) {
        var qty = parseFloat(item.querySelector('.product-qty').value);
        var price = parseFloat(item.querySelector('#product_price').value);
        price = price * qty;
        item.querySelector('#item_total').value = price.toFixed(2);
        total += price;
    });
    document.getElementById('product_grand_total').value = total.toFixed(2);
}

function orderParser(order) {
    return {
        id: order.id,
        date: order.employee_name,
        orderNo: order.employee_name,
        customerName: order.employee_name,
        cost: parseInt(order.employee_salary)
    };
}

function productParser(product) {
    return {
        id: product.id,
        name: product.employee_name,
        unit: product.employee_name,
        price: product.employee_name
    };
}

function productDropParser(product) {
    return {
        id: product.id,
        name: product.title
    };
}

document.addEventListener('DOMContentLoaded', function () {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Fetch JSON data by API call for product drop in order
    axios.get(productsApiUrl)
        .then(response => {
            var data = response.data;
            if (data) {
                // Process the data if needed
                // Example: var products = data.map(productDropParser);
            }
        })
        .catch(error => console.error('Error:', error));

    // Fetch JSON data by API call for UOM list
    var addnew=document.getElementById('openProductModalBtn')
    addnew.addEventListener('click', function () {
        var uomsSelect = document.getElementById('unit');
        axios.get(uomListApiUrl)
            .then(response => {
                var data = response.data;
                //console.log(response.data)
                if (data) {
                    var optionsHTML = '<option value="">--Select--</option>';
                    
                    data.forEach(um => {
                     optionsHTML += `<option value="${um.un_id}">${um.um_name}</option>`;
                  });
                   uomsSelect.innerHTML = optionsHTML;
                }
            })
            .catch(error => console.error('Error:', error));
        });

    // Fetch JSON data by API call for product list
    axios.get(productListApiUrl)
        .then(response => {
            var data = response.data;
            if (data) {
                var tableBody = document.querySelector('table tbody');
                var tableHTML = '';
                data.forEach(product => {
                    tableHTML += `<tr data-id="${product.product_id}" data-name="${product.name}" data-unit="${product.uom_id}" data-price="${product.price_per_unit}">
                        <td>${product.name}</td>
                        <td>${product.um_name}</td>
                        <td>${product.price_per_unit}</td>
                        <td><span class="btn btn-xs btn-danger delete-product">Delete</span></td>
                    </tr>`;
                });
                tableBody.innerHTML = tableHTML;
            }
        })
        .catch(error => console.error('Error:', error));

    // Save Product
    document.getElementById('saveProduct').addEventListener('click', function () {
        // If we found id value in form then update product detail
        var data = new FormData(document.getElementById('productForm'));
        var requestPayload = {
            product_name: null,
            uom_id: null,
            price_per_unit: null
        };
        for (var entry of data.entries()) {
            var element = { name: entry[0], value: entry[1] };
            switch (element.name) {
                case 'name':
                    requestPayload.product_name = element.value;
                    break;
                case 'uoms':
                    requestPayload.uom_id = element.value;
                    break;
                case 'price':
                    requestPayload.price_per_unit = element.value;
                    break;
            }
        }
        callApi('POST', productSaveApiUrl, {
            data: JSON.stringify(requestPayload)
        });
    });

    // Event delegation for delete-product button
    document.querySelector('table tbody').addEventListener('click', function (event) {
        if (event.target.classList.contains('delete-product')) {
            var tr = event.target.closest('tr');
            var data = {
                product_id: tr.dataset.id
            };
            var isDelete = confirm(`Are you sure to delete ${tr.dataset.name} item?`);
            if (isDelete) {
                callApi('POST', productDeleteApiUrl, data);
            }
        }
    });

    document.getElementById('productModal').addEventListener('hide.bs.modal', function () {
        document.getElementById('id').value = '0';
        document.getElementById('name').value = '';
        document.getElementById('unit').value = '';
        document.getElementById('price').value = '';
        document.querySelector('.modal-title').textContent = 'Add New Product';
    });
});
