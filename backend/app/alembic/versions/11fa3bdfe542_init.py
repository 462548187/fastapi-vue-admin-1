"""init

Revision ID: 11fa3bdfe542
Revises: 
Create Date: 2021-03-22 15:45:48.367137

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '11fa3bdfe542'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
  # ### commands auto generated by Alembic - please adjust! ###
  op.create_table('sys_permission', sa.Column('code', sa.String(length=255), nullable=False),
                  sa.Column('conf', postgresql.JSONB(astext_type=sa.Text()), nullable=True), sa.PrimaryKeyConstraint('code'))
  op.create_index(op.f('ix_sys_permission_code'), 'sys_permission', ['code'], unique=False)
  op.create_table('sys_role', sa.Column('id', sa.Integer(), nullable=False), sa.Column('name', sa.String(length=20), nullable=False),
                  sa.Column('description', sa.String(), nullable=True), sa.PrimaryKeyConstraint('id'))
  op.create_index(op.f('ix_sys_role_id'), 'sys_role', ['id'], unique=False)
  op.create_index(op.f('ix_sys_role_name'), 'sys_role', ['name'], unique=True)
  op.create_table('sys_role_permission_rel', sa.Column('role_id', sa.Integer(), nullable=False),
                  sa.Column('permission_code', sa.String(length=255), nullable=False),
                  sa.PrimaryKeyConstraint('role_id', 'permission_code'))
  op.create_index(op.f('ix_sys_role_permission_rel_role_id'), 'sys_role_permission_rel', ['role_id'], unique=False)
  op.create_table('sys_user', sa.Column('id', sa.Integer(), nullable=False), sa.Column('username', sa.String(length=20), nullable=False),
                  sa.Column('fullname', sa.String(length=20), nullable=True), sa.Column('email', sa.String(), nullable=True),
                  sa.Column('password', sa.String(), nullable=False), sa.Column('is_active', sa.Boolean(), nullable=True),
                  sa.Column('is_superuser', sa.Boolean(), nullable=True), sa.PrimaryKeyConstraint('id'))
  op.create_index(op.f('ix_sys_user_id'), 'sys_user', ['id'], unique=False)
  op.create_index(op.f('ix_sys_user_username'), 'sys_user', ['username'], unique=True)
  op.create_table('sys_user_role_rel', sa.Column('user_id', sa.Integer(), nullable=False), sa.Column('role_id',
                                                                                                     sa.Integer(),
                                                                                                     nullable=False),
                  sa.PrimaryKeyConstraint('user_id', 'role_id'))
  op.create_index(op.f('ix_sys_user_role_rel_user_id'), 'sys_user_role_rel', ['user_id'], unique=False)
  # ### end Alembic commands ###


def downgrade():
  # ### commands auto generated by Alembic - please adjust! ###
  op.drop_index(op.f('ix_sys_user_role_rel_user_id'), table_name='sys_user_role_rel')
  op.drop_table('sys_user_role_rel')
  op.drop_index(op.f('ix_sys_user_username'), table_name='sys_user')
  op.drop_index(op.f('ix_sys_user_id'), table_name='sys_user')
  op.drop_table('sys_user')
  op.drop_index(op.f('ix_sys_role_permission_rel_role_id'), table_name='sys_role_permission_rel')
  op.drop_table('sys_role_permission_rel')
  op.drop_index(op.f('ix_sys_role_name'), table_name='sys_role')
  op.drop_index(op.f('ix_sys_role_id'), table_name='sys_role')
  op.drop_table('sys_role')
  op.drop_index(op.f('ix_sys_permission_code'), table_name='sys_permission')
  op.drop_table('sys_permission')
  # ### end Alembic commands ###
