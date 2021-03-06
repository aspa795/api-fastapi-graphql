from orator.migrations import Migration


class CreatePostsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('posts') as table:
            table.increments('id')
            table.integer('userId')
            table.string('title')
            table.text('body')
            table.soft_deletes()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        pass
