from alembic import op
import sqlalchemy as sa


revision = '28487ee2fe86'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Unicode(length=150), nullable=False),
    sa.Column('description', sa.Unicode(), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('tasks')
