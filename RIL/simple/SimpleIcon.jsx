// noinspection JSUnusedGlobalSymbols
export const SimpleIcon = (
    ({icon, title, color = "currentColor", size = "1em", ...others}, ref) => {
        const iconTitle = title ?? icon?.title
        const fillColor = color === "brand" ? "#" + icon?.hex : color

        return (
            <svg
                xmlns="http://www.w3.org/2000/svg"
                width={size}
                height={size}
                fill={fillColor}
                viewBox="0 0 24 24"
                ref={ref}
                {...others}
            >
                <title>{iconTitle}</title>
                <path d={icon?.path}/>
            </svg>
        );
    }
);