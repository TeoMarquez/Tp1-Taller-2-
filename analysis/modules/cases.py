def cases_analysis(df):
    review_col = "review"
    rating_col = "mean of stars"

    df["review_length"] = df[review_col].str.len()

    shortest = df.nsmallest(3, "review_length")
    longest = df.nlargest(3, "review_length")
    low_rating = df.nsmallest(5, rating_col)

    def format_reviews(sub_df):
        formatted = []
        for i, (_, row) in enumerate(sub_df.iterrows(), start=1):
            review = row[review_col]
            rating = row[rating_col]
            length = row["review_length"]

            formatted.append(
                f"{i}. **Rating:** {rating:.2f} | **Longitud:** {length}\n\n"
                f"> {review}\n"
            )
        return "\n".join(formatted)

    return f"""
## Análisis de Casos

### Índice

- [🟢 Reviews cortas](#-3-reviews-cortas)
- [🔴 Reviews largas](#-3-reviews-largas)
- [⚠️ Reviews con bajo rating](#️-5-reviews-con-bajo-rating)


### 🟢 3 Reviews cortas

{format_reviews(shortest)}


### 🔴 3 Reviews largas

{format_reviews(longest)}


### ⚠️ 5 Reviews con bajo rating

{format_reviews(low_rating)}
"""