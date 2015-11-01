require 'test_helper'

class IssuesControllerTest < ActionController::TestCase
  setup do
    @issue = issues(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:issues)
  end

  test "should create issue" do
    assert_difference('Issue.count') do
      post :create, issue: { project: @issue.project, tag: @issue.tag }
    end

    assert_response 201
  end

  test "should show issue" do
    get :show, id: @issue
    assert_response :success
  end

  test "should update issue" do
    put :update, id: @issue, issue: { project: @issue.project, tag: @issue.tag }
    assert_response 204
  end

  test "should destroy issue" do
    assert_difference('Issue.count', -1) do
      delete :destroy, id: @issue
    end

    assert_response 204
  end
end
