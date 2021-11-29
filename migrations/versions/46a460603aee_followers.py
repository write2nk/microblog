"""followers

Revision ID: 46a460603aee
Revises: 5c88fc1d0d22
Create Date: 2021-11-20 16:55:14.594545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46a460603aee'
down_revision = '5c88fc1d0d22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
