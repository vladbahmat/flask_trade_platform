"""empty message

Revision ID: 1c067ac60f98
Revises: 3618502fac70
Create Date: 2021-05-31 15:51:37.212482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c067ac60f98'
down_revision = '3618502fac70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('watchlist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['profile_id'], ['profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('items_watchlists',
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('watchlist_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.ForeignKeyConstraint(['watchlist_id'], ['watchlist.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items_watchlists')
    op.drop_table('watchlist')
    # ### end Alembic commands ###
