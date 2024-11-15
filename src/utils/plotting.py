import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

def plot_scatter_matrix(df, columns, by='exclude', figsize=(6,6)):
    """
    Plot scatter matrix of given dataset excluding/including 
    specified columns.

    Args:
        df: Pandas DataFrame
        columns: list of valid names of columns
        by: 'exclude' if columns have to be excluded, 
        'include' if have to be included (default 
        'exclude')
        figsize: figure size (default (6,6))

    """
    if by == 'exclude' and len(columns)>0:
        data = df.drop(columns=columns)
        # Try to convert to numeric non-numeric columns, 
        # otherwise they are not shown
        for col in data.columns:
            if not pd.api.types.is_numeric_dtype(data[col]):
                try:
                    data[col] = pd.to_numeric(data[col])
                except:
                    pass
        axes = pd.plotting.scatter_matrix(data, figsize=figsize, alpha=1)
        plt.subplots_adjust(wspace=0.4, hspace=0.6)
        for ax in axes[-1, :]:
            ax.tick_params(labelbottom=False)
        for ax in axes[0, :]: 
            ax.xaxis.tick_top()             
            ax.tick_params(labeltop=True)    
            ax.xaxis.set_tick_params(rotation=45)  
        plt.tight_layout()
        plt.show()
    
    elif by == 'include':
        data = df[columns]
        # Try to convert to numeric non-numeric columns, 
        # otherwise they are not shown
        for col in data.columns:
            if not pd.api.types.is_numeric_dtype(data[col]):
                try:
                    data[col] = pd.to_numeric(data[col])
                except:
                    pass
        axes = pd.plotting.scatter_matrix(data, figsize=figsize, alpha=1)
        plt.subplots_adjust(wspace=0.4, hspace=0.6)
        for ax in axes[-1, :]:
            ax.tick_params(labelbottom=False)
        for ax in axes[0, :]: 
            ax.xaxis.tick_top()             
            ax.tick_params(labeltop=True)    
            ax.xaxis.set_tick_params(rotation=45)  
        plt.tight_layout()
        plt.show()
    else:
        # Try to convert to numeric non-numeric columns, 
        # otherwise they are not shown
        for col in data.columns:
            if not pd.api.types.is_numeric_dtype(data[col]):
                try:
                    data[col] = pd.to_numeric(data[col])
                except:
                    pass
        axes = pd.plotting.scatter_matrix(data, figsize=figsize, alpha=1)
        plt.subplots_adjust(wspace=0.4, hspace=0.6)
        for ax in axes[-1, :]:
            ax.tick_params(labelbottom=False)
        for ax in axes[0, :]: 
            ax.xaxis.tick_top()             
            ax.tick_params(labeltop=True)    
            ax.xaxis.set_tick_params(rotation=45)  
        plt.tight_layout()
        plt.show()

def plot_histograms(df, columns, nrows, ncols, figsize=(6,6), scale='normal'):
    """
    Plot histograms for the specified features in df.

    Args:
        df: Pandas DataFrame
        columns: list of valid names of columns
        nrows: number of subplot rows
        ncols: number of subplot columns
        figsize: figure size (default (6,6))
        scale: scale for plot on y-axis 
        (default 'normal') - 'normal'/'log'

    """
    fig = plt.figure(figsize=figsize)

    for pos, col in enumerate(columns):
        ax = plt.subplot(nrows, ncols, pos+1)
        ax.set_xlabel(col)
        ax.set_ylabel('Density')
        title = col + ' distribution'
        kde = sns.kdeplot(data=df, x=col, color='red', ax=ax)
        density_values = kde.lines[0].get_ydata()
        max_density = density_values.max()
        ax.set_xlim([df[col].min(), df[col].max()])
        ax.set_ylim([0, 1.5*max_density])
        ax.set_title(title)
        sns.histplot(data=df, x=col, color='lightskyblue', stat='density')
        plt.grid(visible=True)
        if scale == 'log':
            plt.yscale('log')

    plt.subplots_adjust(wspace=0.4, hspace=0.6)
    plt.show()

def plot_histograms_by_category(df, column, nrows, ncols, feature, figsize=(6,6), scale='normal'):
    """
    Plot histograms for the categories of the specified feature in df.

    Args:
        df: Pandas DataFrame
        column: categorical column name
        nrows: number of subplot rows
        ncols: number of subplot columns
        feature: feature by which doing the plot
        figsize: figure size (default (6,6))
        scale: scale for plot on y-axis 
        (default 'normal') - 'normal'/'log'

    """

    if column not in df.columns or feature not in df.columns:
        raise Exception("Input a valid column.")
    
    categories = df[column].unique()
    categories = categories[~np.isnan(categories)]
    categories = np.sort(categories)

    fig = plt.figure(figsize=figsize)
    for idx, cat in enumerate(categories):
        df_category = df[df[column]==cat]
        ax = plt.subplot(nrows, ncols, idx+1)
        ax.set_xlabel('Actors age')
        ax.set_ylabel('Density')
        title = 'Category [' + str(int(cat)) + ',' + str(int(cat+1)) + ')'
        ax.set_title(title)
        ax.set_yticks([0, 0.07])
        ax.set_ylim([0, 0.07])
        ax.set_xlim([10, 75])
        sns.histplot(data=df_category, x=feature, stat='density', color='lightskyblue')
        sns.kdeplot(data=df_category, x=feature, color='red', ax=ax)

    plt.subplots_adjust(wspace=0.7, hspace=0.9)
    plt.ylabel('Densities')
    plt.show()

