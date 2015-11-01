routerApp.factory('userFactory', function ($http) {
	var o = {}, result = [], users = [] , baseUrl="http://localhost:3000/users";
	o.UserExtractor = function($scope)
	{
		return $http.get(baseUrl);
	}
    o.DeleteUser  = function(id)
    {
        return $http.delete(baseUrl + '/' + id);
    }
 	return o;
});

routerApp.controller('userCtrl',function($scope,$http,userFactory)
{
	userFactory.UserExtractor().success(function(data) {
		$scope.users = angular.copy(data.users);
        $scope.deleteUser = function(id)
        {
            userFactory.DeleteUser(id).success(function()
            {
                userFactory.UserExtractor().success(function(data){
                    $scope.users = angular.copy(data.users);
                });
            });
        }
    });
});