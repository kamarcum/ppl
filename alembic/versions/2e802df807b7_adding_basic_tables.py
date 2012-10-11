"""adding basic tables

Revision ID: 2e802df807b7
Revises: None
Create Date: 2012-09-23 11:13:06.540388

"""

# revision identifiers, used by Alembic.
revision = '2e802df807b7'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('slug', sa.String(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_ts', sa.DateTime(), nullable=True),
    sa.Column('updated_ts', sa.DateTime(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.Column('sign_in_count', sa.Integer(), nullable=True),
    sa.Column('access_token', sa.String(), nullable=False),
    sa.Column('access_token_secret', sa.Text(), nullable=True),
    sa.Column('provider', sa.String(), nullable=True),
    sa.Column('created_ts', sa.DateTime(), nullable=True),
    sa.Column('updated_ts', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('slug', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.Column('created_ts', sa.DateTime(), nullable=True),
    sa.Column('updated_ts', sa.DateTime(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('twitter', sa.String(), nullable=True),
    sa.Column('github_name', sa.String(), nullable=True),
    sa.Column('imported_from_provider', sa.String(), nullable=True),
    sa.Column('imported_from_id', sa.String(), nullable=True),
    sa.Column('reviewed', sa.Boolean(), nullable=True),
    sa.Column('imported_from_screen_nane', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    op.drop_table('users')
    op.drop_table('companies')
    ### end Alembic commands ###
