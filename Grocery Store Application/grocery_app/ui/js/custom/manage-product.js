document.addEventListener('DOMContentLoaded', function () {
    
        var openModalBtn = document.getElementById('openProductModalBtn');
        var closeModalBtns = document.querySelectorAll('#closeProductModalBtn, .modal-overlay');
        var productModal = document.getElementById('productModal');
      
        // Function to open the modal
        function openModal() {
          productModal.style.display = 'block';
        }
      
        // Function to close the modal
        function closeModal() {
          productModal.style.display = 'none';
        }
      
        // Add event listener to open the modal when clicking the button
        openModalBtn.addEventListener('click', openModal);
      
        // Add event listener to close the modal when clicking the close button or overlay
        closeModalBtns.forEach(function (btn) {
          btn.addEventListener('click', closeModal);
        });
    
      
    var productModal = document.getElementById('productModal');
    var addnew=document.getElementById('openProductModalBtn')
// Define your api here
var productListApiUrl = 'http://127.0.0.1:5000/getProducts';
var uomListApiUrl = 'http://127.0.0.1:5000/getUOM';
var productSaveApiUrl = 'http://127.0.0.1:5000/insertProduct';
var productDeleteApiUrl = 'http://127.0.0.1:5000/deleteProduct';
var orderListApiUrl = 'http://127.0.0.1:5000/getAllOrders';
var orderSaveApiUrl = 'http://127.0.0.1:5000/insertOrder';

// For product drop in order
var productsApiUrl = 'https://fakestoreapi.com/products';
    // Get reference to the table body
    var tableBody = document.querySelector('table tbody');

    // Fetch JSON data by API call using Axios
    axios.get(productListApiUrl)
        .then(response => {
            var data = response.data;
            if (data) {
                var tableHTML = '';
                data.forEach(product => {
                    tableHTML += `<tr data-id="${product.product_id}" data-name="${product.name}" data-unit="${product.uom_id}" data-price="${product.price_per_unit}">
                        <td>${product.name}</td>
                        <td>${product.um_name}</td>
                        <td>${product.price_per_unit}</td>
                        <td><span class="btn btn-xs btn-danger delete-product" id="deleteprod">Delete</span></td>
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
            un_id: null,
            price_per_unit: null
        };
        for (var entry of data.entries()) {
            var element = { name: entry[0], value: entry[1] };
            switch (element.name) {
                case 'name':
                    requestPayload.product_name = element.value;
                    break;
                case 'unit':
                    requestPayload.un_id = element.value;
                    break;
                case 'price':
                    requestPayload.price_per_unit = element.value;
                    break;
            }
        }
        axios.post(productSaveApiUrl, {
            data: JSON.stringify(requestPayload)
        })
        .catch(error => console.error('Error:', error));
    });

    // Event delegation for delete-product button
    tableBody.addEventListener('click', function (event) {
        if (event.target.classList.contains('delete-product')) {
            var tr = event.target.closest('tr');
            var data = {
                product_id: tr.dataset.id
            };
            console.log('Data to be sent:', data);
            var isDelete = confirm(`Are you sure to delete ${tr.dataset.name} item?`);
            if (isDelete) {
                axios.post(productDeleteApiUrl, data)
                .catch(error => console.error('Error:', error));
            }
        }
    });

    productModal.addEventListener('hide.bs.modal', function () {
        document.getElementById('id').value = '0';
        document.getElementById('name').value = '';
        document.getElementById('unit').value = '';
        document.getElementById('price').value = '';
        productModal.querySelector('.modal-title').textContent = 'Add New Product';
    });

    // Fetch JSON data by API call for UOM list using Axios
    addnew.addEventListener('click', function () {
    var uomsSelect = document.getElementById('unit');
    axios.get(uomListApiUrl)
        .then(response => {
            var data = response.data;
            
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
});
