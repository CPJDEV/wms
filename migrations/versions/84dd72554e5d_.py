"""empty message

Revision ID: 84dd72554e5d
Revises: cd8c0bc739c5
Create Date: 2018-09-06 17:45:22.669141

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '84dd72554e5d'
down_revision = 'cd8c0bc739c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('warehouse',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.drop_table('feature')
    op.drop_constraint('access_ibfk_1', 'access', type_='foreignkey')
    op.drop_column('access', 'feature_id')
    op.add_column('bin', sa.Column('warehouse_id', sa.Integer(), nullable=True))
    op.drop_constraint('bin_ibfk_1', 'bin', type_='foreignkey')
    op.create_foreign_key(None, 'bin', 'warehouse', ['warehouse_id'], ['id'])
    op.drop_column('bin', 'location_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bin', sa.Column('location_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'bin', type_='foreignkey')
    op.create_foreign_key('bin_ibfk_1', 'bin', 'location', ['location_id'], ['id'])
    op.drop_column('bin', 'warehouse_id')
    op.add_column('access', sa.Column('feature_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('access_ibfk_1', 'access', 'feature', ['feature_id'], ['id'])
    op.create_table('feature',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('section_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['section_id'], ['section.id'], name='feature_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('warehouse')
    # ### end Alembic commands ###
