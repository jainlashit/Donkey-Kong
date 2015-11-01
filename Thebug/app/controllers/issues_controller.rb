class IssuesController < ApplicationController
  before_action :set_issue, only: [:show, :update, :destroy]

  # GET /issues
  # GET /issues.json
  def index
    @issues = Issue.all

    render json: @issues
  end

  # GET /issues/1
  # GET /issues/1.json
  def show
    render json: @issue
  end

  # POST /issues
  # POST /issues.json
  def create
    @issue = Issue.new(issue_params)

    if @issue.save
      render json: @issue, status: :created, location: @issue
    else
      render json: @issue.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /issues/1
  # PATCH/PUT /issues/1.json
  def update
    @issue = Issue.find(params[:id])

    if @issue.update(issue_params)
      head :no_content
    else
      render json: @issue.errors, status: :unprocessable_entity
    end
  end

  # DELETE /issues/1
  # DELETE /issues/1.json
  def destroy
    @issue.destroy

    head :no_content
  end

  private

    def set_issue
      @issue = Issue.find(params[:id])
    end

    def issue_params
      params.require(:issue).permit(:project, :tag)
    end
end
