#include <algorithm>
#include <cmath>
#include "euclideanDistance.hpp"
#include "innerProduct.hpp"
#include "Space.hpp"

namespace chm {
	float Space::getNorm(const float* const data) const {
		auto res = 0.f;

		for(size_t i = 0; i < this->dim; i++)
			res += data[i] * data[i];

		return 1.f / (sqrtf(res) + 1e-30f);
	}

	void Space::normalizeData(const float* const data, float* const res) const {
		const auto norm = this->getNorm(data);

		for(size_t i = 0; i < this->dim; i++)
			res[i] = data[i] * norm;
	}

	uint Space::getCount() const {
		return this->count;
	}

	const float* const Space::getData(const uint id) const {
		return this->data.data() + id * this->dim;
	}

	float Space::getDistance(const uint aID, const uint bID) const {
		return this->getDistance(this->getData(aID), this->getData(bID));
	}

	float Space::getDistance(const float* const a, const float* const b) const {
		return this->distFunc(a, b, this->dim, this->dim4, this->dim16, this->dimLeft);
	}

	float Space::getDistance(const float* const aData, const uint bID) const {
		return this->getDistance(aData, this->getData(bID));
	}

	std::string Space::getDistanceName() const {
		return this->distName;
	}

	uint Space::getLatestID() const {
		return this->count - 1;
	}

	const float* const Space::getNormalizedQuery(const float* const data) {
		if(this->normalize) {
			this->normalizeData(data, this->query.data());
			return this->query.data();
		}

		return data;
	}

	bool Space::isEmpty() const {
		return !this->count;
	}

	const float* const Space::push(const float* const data) {
		float* const res = this->data.data() + this->count * this->dim;

		if(this->normalize)
			this->normalizeData(data, res);
		else
			std::copy(data, data + this->dim, res);

		this->count++;
		return res;
	}

	Space::Space(const size_t dim, const SpaceKind kind, const size_t maxCount)
		: count(0), dim4(dim >> 2 << 2), dim16(dim >> 4 << 4), normalize(kind == SpaceKind::ANGULAR), dim(dim) {

		this->data.resize(this->dim * maxCount);
		const auto info = kind == SpaceKind::EUCLIDEAN
			? getEuclideanInfo(this->dim, this->dim4, this->dim16)
			: getInnerProductInfo(this->dim, this->dim4, this->dim16);

		this->dimLeft = info.dimLeft;
		this->distFunc = info.distFunc;
		this->distName = info.name;

		if(this->normalize)
			this->query.resize(this->dim);
	}
}
