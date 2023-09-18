module.exports = {
    compiler: {
      styledComponents: true,
    },
    reactStrictMode: true,
    transpilePackages: ["ui"],
    async rewrites() {
      return [
        {
          source: "/api/:path*",
          destination: "http://127.0.0.1:8000/api/:path*",
        },
      ];
    },
  };
  