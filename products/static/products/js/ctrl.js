angular.module('productsApp', [])
  .controller('productsController', function($scope, $http, $location){
    /*/angular.element(document).ready(function(){
      $scope.getproducts($location.path());
    })*/
    $scope.data = {};
    $scope.alert = function(mssg){
      alert(mssg);
    };
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
          url = newValue.replace('products/list?', 'products/api/list?format=json&');
        }
        $scope.getproducts(url);
      }
    );

    $scope.update_url = function(category_id){
      url = 'products/list';
      url += "?categories=" + category_id;
      $location.path(url);
    };

    $scope.update_tagurl = function(value, oldvalue)
    {
        
        url = $location.path();
        var regex = new RegExp('tags=' + oldvalue)
        url = url.replace(regex,'tags=' + value); 
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
