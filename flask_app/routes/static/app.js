// Angular application
var app = angular.module('myApp', []);

// Angular controller
app.controller('myCtrl', ['$scope', function($scope){
    $scope.message = 'hello Angular';
    $scope.callMe = function(){
        $scope.message =  'You called me?';
        return $scope.message
    };
}]);
