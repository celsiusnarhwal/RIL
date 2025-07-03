import { defineConfig, mergeConfig } from 'vite';
import baseConfig from './vite.reflex.config.js';
import svgr from 'vite-plugin-svgr';

export default defineConfig(async (env) => {
    const resolvedBase = typeof baseConfig === 'function'
        ? await baseConfig(env)
        : baseConfig;

    const overrides = {
        plugins: [
            svgr({
                svgrOptions: {
                    titleProp: true,
                    dimensions: false,
                },
                include: [
                    '**/node_modules/@material-symbols/svg-*/**/*.svg',
                    '**/node_modules/bootstrap-icons/icons/*.svg',
                ],
            }),
        ],
    };

    return mergeConfig(resolvedBase, overrides)
});