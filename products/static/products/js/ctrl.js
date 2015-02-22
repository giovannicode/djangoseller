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
  })
  .config(function($interpolateProvider, $locationProvider){
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    $locationProvider.html5Mode({
      enabled: true,
      requireBase: false
    })
  })
;
