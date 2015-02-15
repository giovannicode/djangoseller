angular.module('productsApp', [])
  .controller('productsController', function($scope, $http){
    $scope.data = {};
    $scope.alert = function(id){
      alert("ID: " + id);
    }
    $scope.getproducts = function(category_id){
      
      var responsePromise = $http.post(
          "/products/list", 
          $.param({category_id: category_id}),
          { headers: {'Content-Type': 'application/x-www-form-urlencoded'}} 

      );

      responsePromise.success(function(data, status, headers, config){
        $scope.data = JSON.parse(data);
      });
      responsePromise.error(function(data, status, headers, config){
        alert("Ajax failed!"); 
      });
    }
  })
  .config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
  })
;
