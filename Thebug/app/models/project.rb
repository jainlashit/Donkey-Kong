class Project < ActiveRecord::Base
	has_many :issues
	has_many :users
end
