fetch('http://127.0.0.1:5000/')
.then(response => response.text())
.then(data => {
    // Retrieve the base64-encoded image from the server response
    var imageBase64 = data;

    // Create an <img> element and set its source to the image data
    // var imgElement = document.createElement('img');
    // imgElement.src = 'data:image/png;base64,' + imageBase64;

    // Append the <img> element to the graph container
    // var graphContainer = document.getElementById('graph');
    // graphContainer.appendChild(imgElement);
})
.catch(error => {
    console.error('Error:', error);
});

function onPageLoad(){
    console.log("document loaded");
    var url='http://127.0.0.1:5000/get_category_names';
    // var url="/api/get_location_names";
    $.get(url,function(data,status){
        console.log("get_product_names respone received");
        if(data){
            // var product=data.product;
            // var brand=data.brand;
            var category=data.categories;
            var uicategory=document.getElementById('cat');
            $('#cat').empty();
            for(var i in category){
                var opt=new Option(category[i]);
                $('#cat').append(opt);
            }
        }
    });
}
window.onload=onPageLoad;

function fetchBrands(event) {
    event.preventDefault(); // Prevent form submission and page reload
  
    console.log('fetchBrands called');
    var categorySelect = document.getElementById("cat");
    var brandSelect = document.getElementById("brad");
  
    // Clear previous brand options
    brandSelect.innerHTML = "";
  
    // Get selected category value
    var selectedCategory = categorySelect.value;
    console.log(selectedCategory);
  
    // AJAX request to fetch brands for the selected category
    $.ajax({
      url: "http://127.0.0.1:5000/get_brands",
      type: "GET",
      data: { category: selectedCategory },
      success: function (response) {
        var brands = response.brands;
  
        // Add options for each brand
        brands.forEach(function (brand) {
          var option = document.createElement("option");
          option.text = brand;
          brandSelect.add(option);
        });
      },
      error: function (xhr, status, error) {
        console.error(error);
      }
    });
  }
  
  function fetchproduct(event) {
    event.preventDefault(); // Prevent form submission and page reload
  
    console.log('fetchproduct called');
    var categorySelect = document.getElementById("cat");
    var brandSelect = document.getElementById("brad");
    var productSelect = document.getElementById("prod");
  
    // Clear previous brand options
    productSelect.innerHTML = "";
  
    // Get selected category value
    var selectedCategory = categorySelect.value;
    console.log(selectedCategory);

    var selectedbrand = brandSelect.value;
    console.log(selectedbrand);
  
    // AJAX request to fetch brands for the selected category
    $.ajax({
      url: "http://127.0.0.1:5000/get_products",
      type: "GET",
      data: { category: selectedCategory,brand: selectedbrand },
      success: function (response) {
        var product  = response.product;
  
        // Add options for each brand
        product.forEach(function (product) {
          var option = document.createElement("option");
          option.text = product;
          productSelect.add(option);
        });
      },
      error: function (xhr, status, error) {
        console.error(error);
      }
    });
  }

  function optimizedPrice(){
    console.log("optimized price button is clicked");
    var product=$('select#prod.product').val();
    var category=$('select#cat.category').val();
    var brand=$('select#brad.brand').val();
    var discount = $('#dis').val();
    console.log(product);
    console.log(category);
    console.log(brand);
    console.log(discount);
    var optprice=document.getElementById('optimizedPrice');
    var disprice=document.getElementById('discount_');
    var retprice=document.getElementById('retail_price_');
    var optimizeddiscount = document.getElementById('new_discount');
    var url="http://127.0.0.1:5000/predict_price";
    try{
    $.ajax({
        type:    "GET",
        ContentType:"",
        url:  url,
        dataType:'json',
        data:    {
        product: product,
        brand:brand,
        category:category,
        discount:discount
        },
        success: function(data, status) {
          console.log(data.predict_price);
          optprice.innerHTML = "<h2>OPTIMIZED PRICE -" + data.predict_price.toFixed(3).toString() + " Rupees</h2>";
          disprice.innerHTML = "<h2>PREVIOUS DISCOUNT - " + data.discount.toFixed(3).toString() + "% </h2>";
          retprice.innerHTML = "<h2>ORIGINAL RETAIL PRICE -" + data.retail.toFixed(3).toString() + " Rupees</h2>";
          var optimizedDiscount = parseInt(data.retail) - parseInt(data.predict_price);
          var discountPercentage = (optimizedDiscount / parseInt(data.retail)) * 100;
          optimizeddiscount.innerHTML = "<h2>OPTIMIZED DISCOUNT - " + discountPercentage.toFixed(3) + " %</h2>"; 
          console.log(discountPercentage);
          console.log(status);
          var pieData = {
            labels: ['Optimized Discount', 'Remaining'],
            datasets: [{
              data: [discountPercentage, 100 - discountPercentage],
              backgroundColor: ['#ff9999', '#c2c2f0'],
            }]
          };
          var previousDiscountData = {
            labels: ['Previous Discount', 'Remaining'],
            datasets: [{
              data: [data.discount, 100 - data.discount],
              backgroundColor: ['#99ff99', '#f0c2c2'],
              title: {
                display: true,
                text: 'Optimized Discount'
              },
            }]
          };
           // Get the canvas element for the pie chart
      var optimizedDiscountCanvas = document.getElementById('optimizedDiscountChart');
      var previousDiscountCanvas = document.getElementById('previousDiscountChart');
      // Create the pie chart
      optimizedDiscountCanvas.style.width = '1000px';  // Set the desired width
      optimizedDiscountCanvas.style.height = '300px'; 
      previousDiscountCanvas.style.width = '1000px';  // Set the desired width
      previousDiscountCanvas.style.height = '300px'; 
      var optimizedDiscountChart = new Chart(optimizedDiscountCanvas, {
        type: 'pie',
        data: pieData,
        options: {
          title: {
            display: true,
            text: 'Optimized Discount'
          },
          responsive: true,
          maintainAspectRatio: false,  
          width: 500,
          height:100,
          backgroundColor: 'rgba(255, 0, 0, 0.5)'  //
        }
      });
      var previousDiscountChart = new Chart(previousDiscountCanvas, {
        type: 'pie',
        data: previousDiscountData,
        options: {
          title: {
            display: true,
            text: 'Previous Discount'
          },
          responsive: true,
          maintainAspectRatio: false,  
        }
      });
      },
      error: function(xhr, status, error) {
          console.log("AJAX request error:", error);
      }
        });     
    }
    catch(e){
      console.log("error")
    }
}
// function fetchBrands() {
//     console.log('fetchBrands called');
//     // Rest of the code
//   }