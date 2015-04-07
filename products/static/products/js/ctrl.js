angular.module('productsApp', [])
  .controller('productsController', function($scope, $window, $http, $location){
    /*/angular.element(document).ready(function(){
      $scope.getproducts($location.path());
    })*/
    $scope.data = {};
    $scope.alert = function(mssg){
      alert(mssg);
    };
    $scope.goto = function(url){
      $window.location.href = url;
    }
    $scope.$watch(
      function(){
        return $location.path(); 
      }, 
      function(newValue, oldValue){
        if(newValue == '/products/list')
        {
          url = newValue.replace('products/list', 'products/api/list?format=json');
        }
        else
        {
          url_array = newValue.split('/');
          url = newValue.replace(
              '/products/' + url_array[2] +  '/list', 
              '/products/api/list?format=json&categories=' + url_array[2]);
        }
        $scope.getproducts(url);
      }
    );

    $scope.update_url = function(category_id){
      url = 'products/list';
      url += "?categories=" + category_id;
      $location.path(url);
    };

    $scope.update_tagurl = function(value, oldvalue){
        
        url = $location.path();
        if(url == '/products/list'){
            url += '?tags=' +value;
        }
        if(oldvalue == ""){
            url += '&tags=' + value;
        }
        else if(value == ""){
            url = url.replace('&tags=' + oldvalue, '');
        }
        else{
            url = url.replace('tags=' + oldvalue,'tags=' + value); 
        }
        $scope.$apply(function(){
            $location.path(url);
        });
    }

    $scope.update_filterurl = function(type, value){
      url = $location.path();
      var regex = new RegExp(type + '=-?[a-z]+');
      if(url.search(type) != -1)
      {
        url = url.replace(regex, type + "=" + value);
      }
      else
      {
        url += "&" + type + "=" + value;
      }
      $scope.$apply(function(){
        $location.path(url);
      });
    }
      
    $scope.getproducts = function(url){
     
      var responsePromise = $http.get(url);


      responsePromise.success(function(data, status, headers, config){
        $scope.data = data;
      });
      responsePromise.error(function(data, status, headers, config){
        alert("Ajax failed!"); 
      });
    }

    $scope.add_to_cart = function(product_id, csrf_token){
      var responsePromise = $http.get(
        "/carts/add?product_id=" + product_id
      )
 
      responsePromise.success(function(data, status, headers, config){
        alert(data);
      });

      responsePromise.error(function(data, status, headers, config){
        alert('ajax has failed');
      });
    }
        
  })
  .config(function($interpolateProvider, $locationProvider, $httpProvider){
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    $locationProvider.html5Mode({
      enabled: true,
      requireBase: false
    })
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
  })
;
