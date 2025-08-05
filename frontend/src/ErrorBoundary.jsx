import React from 'react';

class ErrorBoundary extends React.Component {
    constructor(props){
        super(props)
        this.state= {hasError: false};
    }
    static gerDerivedStateFromError(error){
        return {hasError: true};
    }

    componentDidCatch(error, errorInfo) {
        console.error("ErrorBoundary caught an error:", error, errorInfo);
    }

    render(){
        return this.state.hasError ? (
            <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                <strong className="font-bold">Something went wrong!</strong>
                <span className="block sm:inline"> Please try again later.</span>
            </div>
        ) : (
            this.props.children
        );
    }
}

export default ErrorBoundary;