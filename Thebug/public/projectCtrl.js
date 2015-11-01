routerApp.factory('projectFactory',function($http)
{
	var o = {},result = [],projects = [], urlBase = "http://localhost:3000/projects";
	o.ProjectExtractor = function($scope)
	{
		return $http.get(urlBase);
	}
    o.Delete = function(id)
    {
        return $http.delete(urlBase + '/' + id);
    }
    return o;
});

routerApp.controller('projectCtrl',function($scope,$http,projectFactory)
{
	projectFactory.ProjectExtractor().success(function(data) {
		$scope.projects = angular.copy(data.projects);
        $scope.deleteProject = function(id)
        {
            projectFactory.Delete(id).success(function()
            {
                    projectFactory.ProjectExtractor().success(function(data) {
                      $scope.projects = angular.copy(data.projects);
                });
            });
        }
	});
});