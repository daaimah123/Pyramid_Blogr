"""init

Revision ID: 8e928db84351
Revises: 68216f1d368b
Create Date: 2019-06-30 19:24:52.150303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e928db84351'
down_revision = '68216f1d368b'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('entries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Unicode(length=255), nullable=False),
    sa.Column('body', sa.UnicodeText(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('edited', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_entries')),
    sa.UniqueConstraint('title', name=op.f('uq_entries_title'))
    )
    op.create_table('models',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_models'))
    )
    op.create_index('my_index', 'models', ['name'], unique=True, mysql_length=255)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=255), nullable=False),
    sa.Column('password', sa.Unicode(length=255), nullable=False),
    sa.Column('last_logged', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('name', name=op.f('uq_users_name'))
    )
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_index('my_index', table_name='models')
    op.drop_table('models')
    op.drop_table('entries')
    # ### end Alembic commands ###
