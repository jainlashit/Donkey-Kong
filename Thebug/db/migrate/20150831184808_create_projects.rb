class CreateProjects < ActiveRecord::Migration
  def change
    create_table :projects do |t|
      t.string :creator
      t.string :name
      t.boolean :is_public

      t.timestamps null: false
    end
  end
end
