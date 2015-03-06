angular.module('cartitemsApp', [])
    .controller('cartitemsController', function($scope, $http, $location){
        $scope.data = {};

        $scope.alert = function(mssg){
            alert(mssg);
        };

        $scope.getcartitems = function(){
            url = '/carts/api/list'
            var responsePromise = $http.get(url);
              
            responsePromise.success(function(data, status, headers, config){
                $scope.data = data;
      
            responsePromise.error(function(data, status, headers, config){
                alert("Ajax failed!")
            });
        }
        $scope.removeitem = function(cartitem_id){
            url = '/carts/delete/' + cartitem_id
            var responsePromise = $http.get(url);

            responsePromise.success(function(data, status, headers, config){
                $scope.data = $scope.getcartitems();
            }

            responsePromise.error(function(data, status, headers, config){
                alert("Ajax failed!")
             });
    })
    .config(function($interpolateProvider){
        $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    })
;
