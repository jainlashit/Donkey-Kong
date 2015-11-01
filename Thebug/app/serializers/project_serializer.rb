class ProjectSerializer < ActiveModel::Serializer
    attributes :id , :creator, :name, :is_public
    has_many :users
    has_many :issues
end
