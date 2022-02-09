from orator.migrations import Migration


class CreateCommentsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('comments') as table:
            table.increments('id')
            table.integer('postId').unsigned().nullable()
            table.foreign('postId').references('id').on('posts').on_update('cascade')
            table.string('name')
            table.text('email')
            table.text('body')
            table.soft_deletes()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        pass
