echo "DEPLOYING FISSION FUNCTION..."
export FISSION_ENVIRONMENT_NAME="env-get-client-nationality"
export FISSION_FUNCTION_NAME="fn-get-client-nationality"
export FISSION_FUNCTION_ROUTE="/get_client_nationality"
export FISSION_TCP_PORT="8000"
echo "RODANDO ARQUIVO configure.sh"; bash configure.sh || { echo "ERROR: Error while running configure.sh [EXITING SCRIPT]"; exit; }
echo "RODANDO ARQUIVO run.sh"; bash run.sh || { echo "ERROR: Error while running run.sh [EXITING SCRIPT]"; exit; }
echo "FISSION DEPLOYED SUCCESSFULLY!"


