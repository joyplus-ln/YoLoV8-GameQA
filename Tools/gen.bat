set WORKSPACE=%cd%

set GEN_CLIENT=%WORKSPACE%\Luban\Luban.dll
set CONF_ROOT=%WORKSPACE%
set DATA_ROOT=%WORKSPACE%\Data
set SERVER_GENROOT=%WORKSPACE%\Data
set GEN_CODE_ROOT=%WORKSPACE%\..\GenCode
set GENJSON_ROOT=%WORKSPACE%\..\Json

echo %WORKSPACE%
dotnet %GEN_CLIENT% ^
    -t all ^
    -c python-json ^
    -d json  ^
    --conf %CONF_ROOT%\luban.conf ^
    -x outputCodeDir=%GEN_CODE_ROOT% ^
    -x outputDataDir=%GENJSON_ROOT% ^
    -x pathValidator.rootDir=D:\workspace2\luban_examples\Projects\Csharp_Unity_bin ^
    -x l10n.textProviderFile=*@D:\workspace2\luban_examples\DesignerConfigs\Datas\l10n\texts.json
pause