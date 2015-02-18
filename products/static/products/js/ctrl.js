angular.module('productsApp', [])
  .controller('productsController', function($scope, $http, $location){
    angular.element(document).ready(function(){
      $scope.getproducts(0);
    })
    $scope.data = {};
    $scope.getproducts = function(category_id){
      url = "/products/api/list?format=json";
      if(!category_id)
      {
      }
      else
      {
        get_param = "categories=" + category_id;
        url += "&" + get_param;
      }
      var responsePromise = $http.get(url);


      responsePromise.success(function(data, status, headers, config){
        $scope.data = data;
        client_url = "/products/list";
        if(!category_id)
        {
          $location.path(client_url);
        } 
        else
        {
          $location.path(client_url + '?' + get_param);
        }
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
