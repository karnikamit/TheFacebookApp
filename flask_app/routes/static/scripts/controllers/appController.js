app.controller('myCtrl', function($scope){
    $scope.message = 'hello Angular';
    $scope.callMe = function(){
        $scope.message =  'You called me?';
        return $scope.message
    };
});
